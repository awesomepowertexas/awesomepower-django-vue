<script setup lang="ts">
import { computed, onMounted, ref, watchEffect } from 'vue'
import PlanCard from '~/components/Plans/PlanCard.vue'
import api from '~/plugins/api'
import global from '~/global'
import { useRoute } from 'vue-router'

const props = defineProps({
  rating: Number,
  term: [Number, String],
  renewable: Boolean,
})

const route = useRoute()

const planList = ref(null)
const loading = ref(true)
const orderBy = ref('med')

const filteredPlans = computed(() => {
  // deep clone
  let plans = global.plans.map((o) => Object.assign({}, o))

  plans = plans
    .filter((o) => o.provider.rating >= props.rating)
    .filter((o) => (props.term === 'All' ? o : o.term === parseInt(props.term)))
    .filter((o) => (props.renewable ? o.percent_renewable >= 99 : o))

  // no prepaid plans
  plans = plans.filter((o) => !o.is_prepaid)

  // fixed rate plans
  plans = plans.filter((o) => o.rate_type === 1)

  // English plans
  plans = plans.filter((o) => o.language === 0)

  plans = plans.sort((a, b) => {
    if (orderBy.value === 'low') {
      return a.low_usage_rate - b.low_usage_rate
    } else if (orderBy.value === 'med') {
      return a.medium_usage_rate - b.medium_usage_rate
    }
    return a.high_usage_rate - b.high_usage_rate
  })

  return plans
})

// Match the plan list parent's height to the plan list, since the plan list
// is absolutely positioned
watchEffect(() => {
  filteredPlans.value

  setTimeout(() => {
    if (planList.value) {
      const { height } = getComputedStyle(planList.value)
      planList.value.parentElement.style.height = height
    }
  })
})

onMounted(async () => {
  if (global.plans.length === 0) {
    const response = await api.get(`/plans?zip_code=${route.params.zip_code}`)
    global.plans = response.data
  }

  loading.value = false
})
</script>

<template>
  <div class="relative">
    <Transition name="fade">
      <div
        v-if="loading"
        key="loading"
        class="absolute w-full flex justify-center"
      >
        <LoadingSpinner :size="50" class="text-blue-500 mt-8" />
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
        ref="planList"
        :key="`plans${filteredPlans.length}${filteredPlans.map(
          (o) => o.ptc_idkey,
        )}`"
        class="absolute w-full flex flex-col"
      >
        <p class="text-gray-700 text-xs mt-4 -mb-4">
          All rates shown are estimates
        </p>

        <PlanCard
          v-for="plan of filteredPlans"
          :key="plan.id"
          :plan="plan"
          :order-by="orderBy"
          class="mt-8"
          @reorder="orderBy = $event"
        />
      </div>
    </Transition>
  </div>
</template>
