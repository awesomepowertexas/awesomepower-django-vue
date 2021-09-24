import Components from 'unplugin-vue-components/vite'
import Icons from 'unplugin-icons/vite'
import { defineConfig } from 'vite'
import istanbul from './vite-plugin-istanbul'
import path from 'path'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  resolve: {
    alias: {
      '~/': `${path.resolve(__dirname, 'src')}/`,
    },
  },

  plugins: [
    istanbul({
      include: ['src/**/*.ts', 'src/**/*.vue'],
    }),
    vue(),
    Components({
      dirs: ['src/components/_global'],
      dts: true,
    }),
    Icons({ compiler: 'vue3' }),
  ],
})
