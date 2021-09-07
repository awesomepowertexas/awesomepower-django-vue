import ViteComponents from 'vite-plugin-components'
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
      include: ['src/**/*.js', 'src/**/*.vue'],
    }),
    vue(),
    ViteComponents({
      dirs: ['src/components/_global'],
      globalComponentsDeclaration: true,
    }),
  ],
})
