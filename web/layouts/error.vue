<template>
  <transition name="error-page">
    <div class="flex flex-col items-center pt-32 md:pt-48">
      <div class="max-w-6xl mx-auto">
        <h1 v-if="error.statusCode === 404">Page not found</h1>

        <h1 v-else>An error has occurred</h1>

        <nuxt-link to="/">
          <app-button class="mt-4">Back to Home</app-button>
        </nuxt-link>
      </div>
    </div>
  </transition>
</template>

<script>
export default {
  layout: 'default',
  props: {
    error: Object,
  },
}
</script>

<style scoped lang="postcss">
.error-page-enter-active {
  transition: opacity 0.3s 0.3s;
}
.error-page-enter,
.error-page-leave-to {
  opacity: 0;
}
</style>
