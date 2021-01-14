import { processGlobEagerImport } from '../utils'
const globalComponents = import.meta.globEager('../components/_global/*.vue')

function registerGlobalComponents(app) {
  const processedGlobalComponents = processGlobEagerImport(globalComponents)

  for (const key in processedGlobalComponents) {
    app.component(key, processedGlobalComponents[key])
  }
}

export default registerGlobalComponents
