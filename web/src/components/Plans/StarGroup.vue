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
      @click="editable ? $emit('set-rating', index) : null"
    />
  </div>
</template>

<script>
import SvgStar from '/src/assets/svg/star.vue'

export default {
  components: {
    SvgStar,
  },

  props: {
    rating: Number,
    editable: {
      type: Boolean,
      default: false,
    },
    lightFill: {
      type: Boolean,
      default: false,
    },
  },

  emits: ['set-rating'],

  data: function () {
    return {
      hovered: null,
    }
  },

  computed: {
    filled() {
      return this.hovered || this.rating
    },
  },
}
</script>

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
