<template>
  <div class="w-full max-w-md bg-blue-800 text-center rounded-xl shadow-md p-5">
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
            v-else-if="error"
            key="error"
            class="absolute w-full h-full flex items-center justify-center"
          >
            <p
              class="font-bold tracking-widest text-red-300 text-xs uppercase pb-1"
            >
              Sorry, something went wrong
            </p>
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
            <router-link :to="`/plans/${zipCode}`">
              <app-button class="btn-green">
                View {{ plans.length }} plans
              </app-button>
            </router-link>
          </div>
        </transition>
      </template>
    </div>
  </div>
</template>

<script>
import api from '/src/plugins/api'

export default {
  data: function () {
    return {
      loading: false,

      zipCode: '',
      plans: [],
      error: false,
    }
  },

  watch: {
    zipCode() {
      this.plans = []
      this.error = false

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
      if ($event.key < '0' || $event.key > '9') {
        $event.preventDefault()
      }
    },

    async getPlans() {
      this.loading = true

      let response
      try {
        response = await api.get(`/plans?zip_code=${this.zipCode}`)
      } catch (error) {
        this.error = true
        this.loading = false
        return
      }

      this.plans = response.data
      this.$store.commit('plans/updateField', {
        path: 'plans',
        value: this.plans,
      })
      this.loading = false
    },

    viewPlans() {
      if (this.plans.length > 0) {
        this.$router.push(`/plans/${this.zipCode}`)
      }
    },
  },
}
</script>
