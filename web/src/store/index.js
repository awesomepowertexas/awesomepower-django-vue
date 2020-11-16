import { createStore } from 'vuex'
import plans from './plans'

const store = createStore({
  modules: {
    plans,
  },
})

export default store
