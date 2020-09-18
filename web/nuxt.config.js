import path from 'path'
import fs from 'fs'

const config = {
  target: 'static',
  loading: false,
  generate: {
    fallback: true,
  },
  buildModules: [
    '@nuxtjs/eslint-module',
    '@nuxtjs/tailwindcss',
    '@nuxtjs/fontawesome',
  ],
  modules: ['@nuxtjs/axios', '@nuxtjs/gtm', '@nuxtjs/sitemap'],
  plugins: ['~/plugins/global'],
  publicRuntimeConfig: {
    axios: {
      baseURL: process.env.API_BASE_URL,
    },
  },
  gtm: {
    id: 'GTM-5MTHZW4',
    pageTracking: true,
  },
  sitemap: {
    hostname: 'https://awesomepowertexas.com',
  },
  fontawesome: {
    icons: {
      solid: ['faChevronCircleDown', 'faChevronCircleUp'],
      brands: ['faFacebookSquare', 'faGithub', 'faTwitterSquare'],
    },
  },
  build: {
    extend: (config) => {
      const svgRule = config.module.rules.find((rule) => rule.test.test('.svg'))

      svgRule.test = /\.(png|jpe?g|gif|webp)$/

      config.module.rules.push({
        test: /\.svg$/,
        use: ['babel-loader', 'vue-svg-loader'],
      })
    },
    babel: {
      babelrc: true,
      configFile: './.babelrc',
    },
  },
  head: {
    titleTemplate: '%s | Awesome Power',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      {
        hid: 'description',
        name: 'description',
        content: 'Find a cheap electricity plan, headache free',
      },
      { property: 'og:title', content: 'Awesome Power Texas' },
      {
        property: 'og:description',
        content: 'Find a cheap electricity plan, headache free',
      },
      { property: 'og:type', content: 'website' },
      { property: 'og:url', content: 'https://awesomepowertexas.com/' },
      {
        property: 'og:image',
        content: 'https://awesomepowertexas.com/og-image.png',
      },
      { property: 'og:image:width', content: '1440' },
      { property: 'og:image:height', content: '754' },
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
      {
        rel: 'stylesheet',
        href:
          'https://fonts.googleapis.com/css2' +
          '?family=Open+Sans:wght@300;400;700' +
          '&family=Solway:wght@300;700' +
          '&display=swap',
      },
      {
        rel: 'apple-touch-icon',
        sizes: '180x180',
        href: '/apple-touch-icon.png',
      },
      {
        rel: 'icon',
        type: 'image/png',
        sizes: '32x32',
        href: '/favicon-32x32.png',
      },
      {
        rel: 'icon',
        type: 'image/png',
        sizes: '16x16',
        href: '/favicon-16x16.png',
      },
      { rel: 'manifest', href: '/site.webmanifest' },
    ],
  },
}

if (process.env.NODE_ENV === 'development') {
  config.server = {
    https: {
      key: fs.readFileSync(
        path.resolve(__dirname, 'local.awesomepowertexas.com-key.pem'),
      ),
      cert: fs.readFileSync(
        path.resolve(__dirname, 'local.awesomepowertexas.com.pem'),
      ),
    },
  }
}

if (process.env.BABEL_ENV === 'test') {
  config.build.babel.plugins = [
    ['istanbul', { extension: ['.js', '.vue'], exclude: ['.nuxt/**'] }],
  ]
}

export default config
