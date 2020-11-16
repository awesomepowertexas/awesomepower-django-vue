import { getField, updateField } from 'vuex-map-fields'

const store = {
  namespaced: true,

  state() {
    return {
      plans: [],
    }
  },

  getters: {
    getField,
  },

  mutations: {
    updateField,
  },
}

export default store
