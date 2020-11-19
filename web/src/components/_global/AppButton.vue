<template>
  <button
    :disabled="loading"
    class="h-10 inline-flex items-center justify-center rounded px-8 font-bold text-white cursor-pointer whitespace-nowrap transition"
  >
    <slot v-if="!loading" />

    <loading-spinner v-else />
  </button>
</template>

<script>
export default {
  props: {
    loading: Boolean,
  },
}
</script>

<style scoped lang="postcss">
button:disabled {
  @apply cursor-not-allowed opacity-75;
}

.btn-blue {
  @apply bg-blue-500;
}
.btn-blue:hover {
  @apply bg-blue-600;
}

.btn-green {
  @apply bg-green-500;
}
.btn-green:hover {
  @apply bg-green-600;
}

.btn-red {
  @apply bg-red-500;
}
.btn-red:hover {
  @apply bg-red-600;
}
</style>
