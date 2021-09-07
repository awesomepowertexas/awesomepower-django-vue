<script setup lang="ts">
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()

function navigateToFaqs() {
  if (route.path === '/') {
    document.getElementById('faqs').scrollIntoView({ behavior: 'smooth' })
  } else {
    router.push({ path: '/', hash: '#faqs' })
  }
}
</script>

<template>
  <div id="footer" class="md:h-40 bg-gray-900 text-white text-sm p-10">
    <div
      class="h-full max-w-4xl flex flex-col md:flex-row md:items-center justify-between mx-auto"
    >
      <div class="flex-1 flex items-center text-3xl">
        <a href="https://www.facebook.com/AwesomePowerTexas/" target="_blank">
          <font-awesome-icon :icon="['fab', 'facebook-square']" />
        </a>

        <a
          href="https://twitter.com/AwesomePowerTX"
          target="_blank"
          class="ml-4"
        >
          <font-awesome-icon :icon="['fab', 'twitter-square']" />
        </a>

        <a
          href="https://github.com/awesomepowertexas/awesomepower"
          target="_blank"
          class="ml-4"
        >
          <font-awesome-icon :icon="['fab', 'github']" />
        </a>
      </div>

      <div
        class="flex-grow flex flex-col md:flex-row md:items-center md:justify-center font-bold mt-6 md:mt-0"
      >
        <router-link to="/">Home</router-link>

        <span
          class="cursor-pointer mt-4 md:mt-0 md:ml-8"
          @click="navigateToFaqs"
        >
          FAQs
        </span>

        <router-link to="/privacy" class="mt-4 md:mt-0 md:ml-8">
          Privacy
        </router-link>

        <router-link to="/terms" class="mt-4 md:mt-0 md:ml-8"
          >Terms</router-link
        >
      </div>

      <div class="flex-1 text-2xs text-gray-500 md:text-right mt-6 md:mt-0">
        Copyright © {{ new Date().getFullYear() }}<br />
        Michael Hays
      </div>
    </div>
  </div>
</template>

<style scoped lang="postcss">
a:hover,
span:hover {
  @apply text-gray-500;
}
</style>
