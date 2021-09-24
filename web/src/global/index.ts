import { reactive } from 'vue'

interface Global {
  plans: any[]
  resetState(): void
}

function getDefaultState(): Global {
  return {
    plans: [],

    /**
     * Reset the state object to its initial value.
     *
     * This must be done without reassigning global, in order to retain its
     * reactivity.
     */
    resetState() {
      global = this

      for (const key in global) {
        /* istanbul ignore else */
        if (Object.prototype.hasOwnProperty.call(global, key)) {
          delete global[key]
        }
      }

      Object.assign(global, getDefaultState())
    },
  }
}

let global = reactive(getDefaultState())

export default global
