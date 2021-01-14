import istanbulInstrument from 'istanbul-lib-instrument'
import { createFilter } from '@rollup/pluginutils'

export default function istanbul(options) {
  const filter = createFilter(options.include, options.exclude)

  return {
    name: 'istanbul',

    transform(src, id) {
      if (
        process.env.NODE_ENV == 'production' ||
        id.startsWith('/@modules/') ||
        id.includes('node_modules') ||
        !filter(id)
      ) {
        return
      }

      let scriptSrc = src
      let scriptStartIndex
      let scriptEndIndex

      if (id.endsWith('.vue')) {
        scriptStartIndex = src.indexOf('<script>')
        scriptEndIndex = src.indexOf('</script>')

        if (scriptStartIndex === -1 || scriptEndIndex === -1) {
          return
        }

        scriptStartIndex += '<script>'.length

        const numNewlines = (src.slice(0, scriptStartIndex).match(/\n/g) || [])
          .length
        scriptSrc =
          '\n'.repeat(numNewlines) + src.slice(scriptStartIndex, scriptEndIndex)
      }

      const instrumenter = new istanbulInstrument.createInstrumenter({
        esModules: true,
        compact: true,
        produceSourceMap: true,
        autoWrap: true,
        preserveComments: true,
      })

      let code = instrumenter.instrumentSync(scriptSrc, id)

      if (id.endsWith('.vue')) {
        code =
          src.slice(0, scriptStartIndex) +
          '\n' +
          code +
          '\n' +
          src.slice(scriptEndIndex)
      }

      return code
    },

    configureServer({ app }) {
      app.use('/__coverage__', (req, res) => {
        const coverage = global.__coverage__ || null

        res.end(JSON.stringify({ coverage }))
      })
    },
  }
}
