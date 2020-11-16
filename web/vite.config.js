const istanbul = require('vite-plugin-istanbul')

module.exports = {
  plugins: [
    istanbul({
      include: 'src/*',
      extension: ['.js', '.vue'],
    }),
  ],
}
