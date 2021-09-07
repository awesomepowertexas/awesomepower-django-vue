<script setup lang="ts">
import Filter from '~/components/Plans/Filter.vue'
import PlanList from '~/components/Plans/PlanList.vue'
import { ref } from 'vue'
import { useHead } from '@vueuse/head'
import { useRoute } from 'vue-router'

useHead({ title: 'Plans' })

const route = useRoute()

// Filter options
const termOptions = ['All', 1, 3, 6, 12, 18, 24, 36] as const
type TermOptions = typeof termOptions[number]
const rating = ref(1)
const term = ref<TermOptions>(12)
const renewable = ref(false)
</script>

<template>
  <div class="bg-blue-100 pt-20 md:pt-48 px-4 pb-8 md:pb-20">
    <div class="w-full max-w-3xl mx-auto">
      <h1 class="font-solway font-bold text-2xl md:text-4xl">
        Plans for {{ route.params.zip_code }}
      </h1>

      <div class="w-10 md:w-20 h-1 bg-blue-300" />

      <Filter
        v-model:rating="rating"
        v-model:term="term"
        v-model:renewable="renewable"
        :term-options="termOptions"
      />

      <PlanList :rating="rating" :term="term" :renewable="renewable" />
    </div>
  </div>
</template>
