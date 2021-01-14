import istanbul from './vite-plugin-istanbul'
import vue from '@vitejs/plugin-vue'

module.exports = {
  plugins: [
    istanbul({
      include: ['src/**/*.js', 'src/**/*.vue'],
    }),
    vue(),
  ],
}
