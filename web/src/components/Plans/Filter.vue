<script setup lang="ts">
import StarGroup from '~/components/Plans/StarGroup.vue'
import { termOptions } from '~/types'
import { useVModels } from '@vueuse/core'

const props = defineProps<{
  rating: number
  term: typeof termOptions[number]
  renewable: boolean
}>()

const emits = defineEmits<{
  (e: 'update:rating', rating: number): void
  (e: 'update:term', term: typeof termOptions[number]): void
  (e: 'update:renewable', renewable: boolean): void
}>()

const { rating, term, renewable } = useVModels(props, emits)
</script>

<template>
  <!-- eslint-disable vue/no-mutating-props -->
  <h2
    class="text-center font-bold text-sm text-blue-900 uppercase tracking-widest mt-4 md:mt-8"
  >
    Filter
  </h2>

  <div
    class="bg-blue-700 rounded font-bold text-sm text-white flex flex-wrap justify-between mt-2 px-4 pb-4"
  >
    <StarGroup
      id="input-stars"
      v-model:rating="rating"
      :editable="true"
      light-fill
      class="mt-4"
    />

    <div class="flex items-center mt-4">
      <select id="select-term" v-model="term" class="text-gray-900">
        <option v-for="option of termOptions" :key="option" :value="option">
          {{ option }}
        </option>
      </select>

      <label for="select-term" class="ml-1">month term</label>
    </div>

    <div class="flex items-center mt-4">
      <input id="input-renewable" v-model="renewable" type="checkbox" />

      <label for="input-renewable" class="ml-1">100% renewable</label>
    </div>
  </div>
  <!-- eslint-enable -->
</template>
