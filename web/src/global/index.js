import { reactive } from 'vue'

function getDefaultState() {
  return {
    plans: [],
  }
}

/**
 * Reset the state object to its initial value.
 *
 * This must be done without reassigning global, in order to retain its
 * reactivity.
 */
function resetState() {
  global = this

  for (const key in global) {
    /* istanbul ignore else */
    if (Object.prototype.hasOwnProperty.call(global, key)) {
      delete global[key]
    }
  }

  Object.assign(global, getDefaultState())
  global.resetState = resetState
}

let global = reactive({})
global.resetState = resetState
global.resetState()

export default global
