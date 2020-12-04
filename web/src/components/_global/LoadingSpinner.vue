<template>
  <svg
    viewBox="0 0 100 100"
    preserveAspectRatio="xMidYMid"
    data-icon="loading-spinner"
    :width="`${size}px`"
    :height="`${size}px`"
  >
    <circle
      cx="50"
      cy="50"
      fill="none"
      stroke="currentColor"
      stroke-width="10"
      r="35"
      stroke-dasharray="164.93361431346415 56.97787143782138"
      transform="rotate(246.466 50 50)"
    >
      <animateTransform
        attributeName="transform"
        type="rotate"
        repeatCount="indefinite"
        dur="1s"
        values="0 50 50;360 50 50"
        keyTimes="0;1"
      />
    </circle>
  </svg>
</template>

<script>
export default {
  name: 'LoadingSpinner',

  props: {
    size: {
      type: Number,
      default: 20,
    },
  },
}
</script>
