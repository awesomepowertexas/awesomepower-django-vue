import globalComponents from 'globby!../components/_global/*.vue'

function registerGlobalComponents(app) {
  for (const key in globalComponents) {
    const component = globalComponents[key]

    app.component(component.name, component)
  }
}

export default registerGlobalComponents
