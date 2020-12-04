const istanbul = require('./vite-plugin-istanbul')
const globbyImport = require('vite-transform-globby-import')

module.exports = {
  plugins: [
    istanbul({
      include: 'src/*',
      extension: ['.js', '.vue'],
    }),
  ],
  transforms: [globbyImport({})],
}
