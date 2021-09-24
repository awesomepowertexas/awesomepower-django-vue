<script setup lang="ts">
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()

function navigateToFaqs() {
  if (route.path === '/') {
    document.getElementById('faqs')?.scrollIntoView({ behavior: 'smooth' })
  } else {
    router.push({ path: '/', hash: '#faqs' })
  }
}
</script>

<template>
  <div id="header" class="flex items-end px-5 md:px-12">
    <div
      class="z-20 w-full max-w-6xl flex items-center justify-between mx-auto"
    >
      <router-link to="/">
        <img
          id="header-logo"
          src="/src/assets/svg/logo.svg"
          class="w-48 md:w-80"
        />
      </router-link>

      <span
        class="cursor-pointer font-bold text-sm hover:text-blue-700 mb-1"
        @click="navigateToFaqs"
      >
        FAQs
      </span>
    </div>
  </div>
</template>

<style scoped lang="postcss">
#header-logo:hover > path:nth-child(3) {
  fill: hsl(207, 90%, 96%);
}
</style>
