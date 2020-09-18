<template>
  <div class="w-full max-w-md bg-blue-800 text-center rounded-2xl shadow p-5">
    <p
      class="h-10 flex items-center justify-center font-solway font-bold text-white md:text-xl uppercase"
    >
      View plans in your zip code
    </p>

    <input
      ref="input"
      v-model="zipCode"
      :disabled="loading"
      type="text"
      class="w-56 h-16 rounded-lg text-3xl text-gray-800 font-solway font-light text-center my-4"
      placeholder="12345"
      maxlength="5"
      @keypress="onlyNumber"
      @keypress.enter="viewPlans"
    />

    <div class="h-10 relative">
      <template v-if="zipCode.length === 5">
        <transition name="fade">
          <div
            v-if="loading"
            key="loading"
            class="absolute w-full h-full flex items-center justify-center"
          >
            <loading-spinner class="text-white" />
          </div>

          <div
            v-else-if="plans.length === 0"
            key="no-plans"
            class="absolute w-full h-full flex items-center justify-center"
          >
            <p
              class="font-bold tracking-widest text-red-300 text-xs uppercase pb-1"
            >
              No plans found for this zip code
            </p>
          </div>

          <div
            v-else
            key="plans"
            class="absolute w-full h-full flex items-center justify-center"
          >
            <nuxt-link :to="`/plans/${zipCode}`">
              <app-button class="btn-green">
                View {{ plans.length }} plans
              </app-button>
            </nuxt-link>
          </div>
        </transition>
      </template>
    </div>
  </div>
</template>

<script>
export default {
  data: () => ({
    loading: false,

    zipCode: '',
    plans: [],
  }),

  watch: {
    zipCode() {
      this.plans = []

      if (this.zipCode.length === 5) {
        this.getPlans()
      }
    },
  },

  mounted() {
    this.$refs.input.focus()
  },

  methods: {
    onlyNumber($event) {
      const keyCode = $event.keyCode ? $event.keyCode : $event.which
      if (keyCode < 48 || keyCode > 57) {
        $event.preventDefault()
      }
    },

    async getPlans() {
      this.loading = true

      try {
        const response = await this.$axios.$get(
          `/plans?zip_code=${this.zipCode}`,
        )

        this.plans = response
        this.$store.commit('plans/set', this.plans)
        this.loading = false
      } catch (error) {
        alert('Sorry, something went wrong.')
      }
    },

    viewPlans() {
      if (this.plans.length > 0) {
        this.$router.push(`/plans/${this.zipCode}`)
      }
    },
  },
}
</script>
