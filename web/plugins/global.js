import Vue from 'vue'

// globally register every component in components/global
const requireComponent = require.context(
  '../components/global',
  false,
  /\w+\.(vue)$/,
)

requireComponent.keys().forEach((fileName) => {
  const componentName = fileName.substring(2, fileName.length - 4)
  const componentConfig = requireComponent(fileName)

  Vue.component(componentName, componentConfig.default || componentConfig)
})
