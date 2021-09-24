<script setup lang="ts">
import { computed, ref } from 'vue'
import SvgStar from '~/assets/svg/star.vue'

interface Props {
  rating: number
  editable?: boolean
  lightFill?: boolean
}

const props = withDefaults(defineProps<Props>(), {
  editable: false,
  lightFill: false,
})

const _emits = defineEmits<{
  (e: 'update:rating', rating: number): void
}>()

const activeHoverIndex = ref(-1)

const filled = computed(() => {
  return activeHoverIndex.value !== -1 ? activeHoverIndex.value : props.rating
})
</script>

<template>
  <div class="flex">
    <svg-star
      v-for="index of [1, 2, 3, 4, 5]"
      :key="index"
      :class="[
        filled >= index ? 'filled' : 'text-transparent',
        editable ? 'cursor-pointer' : '',
        lightFill ? 'light-fill' : '',
      ]"
      class="h-6"
      @mouseenter="editable ? (activeHoverIndex = index) : null"
      @mouseleave="editable ? (activeHoverIndex = -1) : null"
      @click="editable ? $emit('update:rating', index) : null"
    />
  </div>
</template>

<style scoped lang="postcss">
.filled {
  color: #dbc900;
}

svg.light-fill > path {
  stroke: #ecee88;
}
.filled.light-fill {
  color: #ecee88;
}
</style>
