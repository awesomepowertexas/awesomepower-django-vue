<template>
  <svg-loading-spinner :width="`${size}px`" :height="`${size}px`" />
</template>

<script>
import SvgLoadingSpinner from '@/assets/svg/loading-spinner.svg'

export default {
  components: {
    SvgLoadingSpinner,
  },

  props: {
    size: {
      type: Number,
      default: 20,
    },
  },
}
</script>
