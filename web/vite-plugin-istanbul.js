const babel = require('@babel/core')
const BabelPluginIstanbul = require('babel-plugin-istanbul')
const TestExclude = require('test-exclude')

function createTransform(opts) {
  let exclude
  const plugins = [[BabelPluginIstanbul, opts]]
  const cwd = process.cwd()

  return {
    test(ctx) {
      if (ctx.isBuild || process.env.NODE_ENV == 'production') {
        return false
      } else if (
        ctx.path.startsWith('/@modules/') ||
        ctx.path.includes('node_modules')
      ) {
        return false
      } else if (!exclude) {
        exclude = new TestExclude({
          cwd,
          include: opts.include,
          exclude: opts.exclude,
          extension: opts.extension,
          excludeNodeModules: true,
        })
      }

      return exclude.shouldInstrument(ctx.path)
    },
    transform(ctx) {
      const { code, map } = babel.transformSync(ctx.code, {
        plugins,
        cwd,
        ast: false,
        sourceMaps: true,
        filename: ctx.path,
      })

      return { code, map }
    },
  }
}

const serverPlugin = ({ app }) => {
  app.use(async (ctx, next) => {
    if (ctx.path === '/__coverage__') {
      const coverage = global.__coverage__ ?? null

      ctx.status = 200
      ctx.type = 'json'
      ctx.body = { coverage }
    } else {
      await next()
    }
  })
}

function istanbulPlugin(opts) {
  const transform = createTransform(opts)

  return {
    transforms: [transform],
    configureServer: serverPlugin,
  }
}

module.exports = istanbulPlugin
