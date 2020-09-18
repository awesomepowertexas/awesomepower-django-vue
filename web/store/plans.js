export const state = () => ({
  plans: [],
})

export const mutations = {
  set(state, plans) {
    state.plans = plans
  },
}
