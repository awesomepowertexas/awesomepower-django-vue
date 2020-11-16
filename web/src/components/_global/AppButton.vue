<template>
  <button :disabled="loading" class="btn">
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
.btn {
  @apply flex items-center justify-center bg-gray-500 font-bold text-white cursor-pointer rounded h-10 px-8;
  transition: background-color 0.3s, filter 0.3s, opacity 0.3s;
}
.btn:hover {
  @apply bg-gray-600;
}
.btn:disabled {
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
