function processGlobEagerImport(importObj) {
  const processedImportObj = {}

  for (const key in importObj) {
    const componentName = key
      .split('/')
      .slice(-1)[0]
      .split('.')
      .slice(0, -1)
      .join('')

    processedImportObj[componentName] = importObj[key].default
  }

  return processedImportObj
}

export { processGlobEagerImport }
