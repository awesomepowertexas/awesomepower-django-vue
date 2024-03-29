<script setup lang="ts">
import { Plan } from '~/types'
import StarGroup from '~/components/Plans/StarGroup.vue'
import { computed } from 'vue'

type OrderBy = 'low' | 'med' | 'high'

const props = defineProps<{
  plan: Plan
  orderBy: string
}>()

const _emits = defineEmits<{
  (e: 'reorder', orderBy: OrderBy): void
}>()

const mainUsageRate = computed(() => {
  if (props.orderBy === 'low') {
    return props.plan.low_usage_rate
  } else if (props.orderBy === 'med') {
    return props.plan.medium_usage_rate
  }
  return props.plan.high_usage_rate
})
</script>

<template>
  <div class="plan-card bg-white rounded shadow p-4 md:p-6">
    <!-- Desktop -->
    <div class="hidden md:flex">
      <div class="w-40 flex-shrink-0 flex flex-col items-center">
        <img
          :src="`/provider-images/${plan.provider.name}.png`"
          :alt="plan.provider.name"
          class="w-40 h-24 object-contain mt-4"
        />

        <StarGroup :rating="plan.provider.rating" class="mt-2" />
      </div>

      <div class="flex-grow flex flex-col ml-4">
        <p class="font-bold leading-tight overflow-hidden">
          {{ plan.name }}
        </p>

        <p class="text-sm text-gray-700 mt-2">
          {{ plan.term }} month term · {{ plan.percent_renewable }}% renewable
        </p>

        <p v-if="plan.is_new_customer" class="text-sm text-orange-500 mt-2">
          <i>New customers only</i>
        </p>

        <div class="flex-grow" />

        <div class="flex items-center mt-4">
          <a :href="plan.enroll_url" target="_blank">
            <AppButton class="btn-green">Sign up</AppButton>
          </a>

          <a :href="plan.facts_url" class="text-blue-600 ml-6" target="_blank">
            Facts
          </a>

          <a :href="plan.terms_url" class="text-blue-600 ml-6" target="_blank">
            Terms
          </a>
        </div>
      </div>

      <div class="w-64 flex items-center ml-4">
        <div class="flex-1 flex flex-col items-center">
          <div class="flex items-center">
            <p
              class="cursor-pointer font-bold text-gray-500 text-xs uppercase"
              @click="$emit('reorder', orderBy === 'low' ? 'med' : 'low')"
            >
              {{ orderBy === 'low' ? 'med' : 'low' }}
            </p>

            <p class="font-solway font-light text-2xl ml-2">
              {{
                (
                  (orderBy === 'low'
                    ? parseFloat(plan.medium_usage_rate)
                    : parseFloat(plan.low_usage_rate)) * 100
                ).toFixed(1)
              }}¢
            </p>
          </div>

          <div class="flex items-center mt-4">
            <p
              class="cursor-pointer font-bold text-gray-500 text-xs uppercase"
              @click="$emit('reorder', orderBy === 'high' ? 'med' : 'high')"
            >
              {{ orderBy === 'high' ? 'med' : 'high' }}
            </p>

            <p class="font-solway font-light text-2xl ml-2">
              {{
                (
                  (orderBy === 'high'
                    ? parseFloat(plan.medium_usage_rate)
                    : parseFloat(plan.high_usage_rate)) * 100
                ).toFixed(1)
              }}¢
            </p>
          </div>
        </div>

        <div class="flex-1 flex flex-col items-center">
          <p class="font-bold text-blue-700 text-xs uppercase">
            {{ orderBy }}
          </p>

          <p class="font-solway font-light text-5xl">
            {{ (parseFloat(mainUsageRate) * 100).toFixed(1) }}¢
          </p>

          <p class="font-bold text-gray-500 text-xs uppercase">per kWh</p>
        </div>
      </div>
    </div>

    <!-- Mobile -->
    <div class="md:hidden flex flex-col">
      <div class="text-center">
        <p class="font-bold text-lg">{{ plan.name }}</p>
      </div>

      <div class="flex items-center mt-6">
        <div class="flex-1 flex flex-col items-center">
          <img
            :src="`/provider-images/${plan.provider.name}.png`"
            :alt="plan.provider.name"
            class="w-40 h-24 object-contain"
          />

          <StarGroup :rating="plan.provider.rating" class="mt-4" />
        </div>

        <div class="flex-1 text-sm ml-6">
          <p class="text-gray-700">{{ plan.term }} month term</p>

          <p class="text-gray-700 mt-3">
            {{ plan.percent_renewable }}% renewable
          </p>

          <p v-if="plan.is_new_customer" class="text-sm text-orange-500 mt-3">
            <i>New customers only</i>
          </p>

          <div class="flex mt-3">
            <a :href="plan.facts_url" class="text-blue-600" target="_blank">
              Facts
            </a>

            <span class="text-gray-600 mx-2">·</span>

            <a :href="plan.terms_url" class="text-blue-600" target="_blank">
              Terms
            </a>
          </div>
        </div>
      </div>

      <div class="flex items-center mt-8">
        <div class="flex-1 flex flex-col items-center">
          <div class="flex items-center">
            <p
              class="cursor-pointer font-bold text-gray-500 text-xs uppercase"
              @click="$emit('reorder', orderBy === 'low' ? 'med' : 'low')"
            >
              {{ orderBy === 'low' ? 'med' : 'low' }}
            </p>

            <p class="font-solway font-light text-2xl ml-2">
              {{
                (
                  (orderBy === 'low'
                    ? parseFloat(plan.medium_usage_rate)
                    : parseFloat(plan.low_usage_rate)) * 100
                ).toFixed(1)
              }}¢
            </p>
          </div>

          <div class="flex items-center mt-4">
            <p
              class="cursor-pointer font-bold text-gray-500 text-xs uppercase"
              @click="$emit('reorder', orderBy === 'high' ? 'med' : 'high')"
            >
              {{ orderBy === 'high' ? 'med' : 'high' }}
            </p>

            <p class="font-solway font-light text-2xl ml-2">
              {{
                (
                  (orderBy === 'high'
                    ? parseFloat(plan.medium_usage_rate)
                    : parseFloat(plan.high_usage_rate)) * 100
                ).toFixed(1)
              }}¢
            </p>
          </div>
        </div>

        <div class="flex-1 flex flex-col items-center">
          <p class="font-bold text-blue-700 text-xs uppercase">
            {{ orderBy }}
          </p>

          <p class="font-solway font-light text-5xl">
            {{ (parseFloat(mainUsageRate) * 100).toFixed(1) }}¢
          </p>

          <p class="font-bold text-gray-500 text-xs uppercase">per kWh</p>
        </div>
      </div>

      <a :href="plan.enroll_url" target="_blank" class="mt-8">
        <AppButton class="btn-green w-full">Sign up</AppButton>
      </a>
    </div>
  </div>
</template>
