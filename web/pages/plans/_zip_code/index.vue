<template>
  <div class="bg-blue-100 pt-20 md:pt-48 px-4 pb-8 md:pb-20">
    <div class="w-full max-w-3xl mx-auto">
      <h1 class="font-solway font-bold text-2xl md:text-4xl">
        Plans for {{ $route.params.zip_code }}
      </h1>

      <div class="w-10 md:w-20 h-1 bg-blue-300" />

      <h2
        class="text-center font-bold text-sm text-blue-900 uppercase tracking-widest mt-4 md:mt-8"
      >
        Filter
      </h2>

      <div
        class="bg-blue-700 rounded-lg font-bold text-sm text-white flex flex-wrap justify-between mt-2 px-4 pb-4"
      >
        <star-group
          id="input-stars"
          :editable="true"
          :rating="filter.rating"
          light-fill
          class="mt-4"
          @set-rating="filter.rating = $event"
        />

        <div class="flex items-center mt-4">
          <select id="select-term" v-model="filter.term" class="text-gray-900">
            <option value="all">All</option>
            <option :value="1">1</option>
            <option :value="3">3</option>
            <option :value="6">6</option>
            <option :value="12">12</option>
            <option :value="18">18</option>
            <option :value="24">24</option>
            <option :value="36">36</option>
          </select>

          <label for="select-term" class="ml-1">month term</label>
        </div>

        <div class="flex items-center mt-4">
          <input
            id="input-renewable"
            v-model="filter.renewable"
            type="checkbox"
          />

          <label for="input-renewable" class="ml-1">100% renewable</label>
        </div>
      </div>

      <div class="relative">
        <transition name="fade">
          <div
            v-if="loading"
            key="loading"
            class="absolute w-full flex justify-center"
          >
            <loading-spinner :size="50" class="text-blue-500 mt-8" />
          </div>

          <div
            v-else-if="filteredPlans.length === 0"
            key="no-plans"
            class="absolute w-full"
          >
            <p class="text-center text-gray-700 mt-8">
              No plans found for the given filters
            </p>
          </div>

          <div
            v-else
            ref="list"
            :key="`plans${filteredPlans.length}${filteredPlans.map(
              (o) => o.ptc_idkey,
            )}`"
            class="absolute w-full flex flex-col"
          >
            <p class="text-gray-700 text-xs mt-4 -mb-4">
              All rates shown are estimates
            </p>

            <plan-card
              v-for="plan of filteredPlans"
              :key="plan.id"
              :plan="plan"
              :order-by="orderBy"
              class="mt-8"
              @reorder="orderBy = $event"
            />
          </div>
        </transition>
      </div>
    </div>
  </div>
</template>

<script>
import PlanCard from '@/components/Plans/PlanCard.vue'
import StarGroup from '@/components/Plans/StarGroup.vue'

export default {
  components: {
    PlanCard,
    StarGroup,
  },

  data: () => ({
    loading: true,

    plans: [],
    filter: {
      rating: 1,
      term: 12,
      renewable: false,
    },
    orderBy: 'med',
  }),

  computed: {
    filteredPlans() {
      // deep clone
      let plans = this.plans.map((o) => Object.assign({}, o))

      // preferences filter
      plans = plans
        .filter((o) => o.provider.rating >= this.filter.rating)
        .filter((o) =>
          this.filter.term !== 'all' ? o.term === this.filter.term : o,
        )
        .filter((o) => (this.filter.renewable ? o.percent_renewable >= 99 : o))

      // no prepaid plans
      plans = plans.filter((o) => !o.is_prepaid)

      // fixed rate plans
      plans = plans.filter((o) => o.rate_type === 1)

      // English plans
      plans = plans.filter((o) => o.language === 0)

      plans = plans.sort((a, b) => {
        if (this.orderBy === 'low') {
          return a.low_usage_rate - b.low_usage_rate
        } else if (this.orderBy === 'med') {
          return a.medium_usage_rate - b.medium_usage_rate
        }
        return a.high_usage_rate - b.high_usage_rate
      })

      return plans
    },
  },

  created() {
    if (this.$store.state.plans.plans.length > 0) {
      this.plans = this.$store.state.plans.plans
      this.loading = false
    } else {
      this.getPlans()
    }
    this.setListHeight()
  },

  methods: {
    async getPlans() {
      const response = await this.$axios.$get(
        `/plans?zip_code=${this.$route.params.zip_code}`,
      )

      this.plans = response
      this.loading = false
    },

    setListHeight() {
      if (this.$refs.list) {
        const { height } = getComputedStyle(this.$refs.list)
        this.$refs.list.parentElement.style.height = height
      }

      setTimeout(() => {
        this.setListHeight()
      }, 10)
    },
  },

  head: {
    title: 'Plans',
  },
}
</script>
