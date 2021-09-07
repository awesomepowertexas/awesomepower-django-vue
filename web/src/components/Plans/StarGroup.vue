<script setup lang="ts">
import { computed, ref } from 'vue'
import SvgStar from '~/assets/svg/star.vue'

const props = defineProps({
  rating: Number,
  editable: {
    type: Boolean,
    default: false,
  },
  lightFill: {
    type: Boolean,
    default: false,
  },
})

const _emits = defineEmits(['update:rating'])

const hovered = ref(null)

const filled = computed(() => {
  return hovered.value || props.rating
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
      @mouseenter="editable ? (hovered = index) : null"
      @mouseleave="editable ? (hovered = null) : null"
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
