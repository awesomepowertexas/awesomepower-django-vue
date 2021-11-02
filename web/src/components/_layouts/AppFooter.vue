<script setup lang="ts">
import { useRoute, useRouter } from 'vue-router'
import IconFacebookSquare from '~icons/fa-brands/facebook-square'
import IconGithub from '~icons/fa-brands/github'
import IconTwitterSquare from '~icons/fa-brands/twitter-square'

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
  <div id="footer" class="md:h-40 bg-gray-900 text-white text-sm p-10">
    <div
      class="h-full max-w-4xl flex flex-col gap-6 md:flex-row md:items-center justify-between mx-auto"
    >
      <div class="flex-1 flex items-center gap-4 text-3xl">
        <a
          href="https://www.facebook.com/AwesomePowerTexas/"
          target="_blank"
          class="hover:text-gray-500 transition"
        >
          <IconFacebookSquare />
        </a>

        <a
          href="https://twitter.com/AwesomePowerTX"
          target="_blank"
          class="hover:text-gray-500 transition"
        >
          <IconTwitterSquare />
        </a>

        <a
          href="https://github.com/awesomepowertexas/awesomepower"
          target="_blank"
          class="hover:text-gray-500 transition"
        >
          <IconGithub />
        </a>
      </div>

      <div
        class="flex-grow flex flex-col items-start gap-4 md:flex-row md:items-center md:justify-center md:gap-8"
      >
        <router-link to="/" class="font-bold hover:text-gray-500 transition">
          Home
        </router-link>

        <button
          class="cursor-pointer font-bold hover:text-gray-500 transition"
          @click="navigateToFaqs"
        >
          FAQs
        </button>

        <router-link
          to="/privacy"
          class="font-bold hover:text-gray-500 transition"
        >
          Privacy
        </router-link>

        <router-link
          to="/terms"
          class="font-bold hover:text-gray-500 transition"
        >
          Terms
        </router-link>
      </div>

      <div class="flex-1 text-2xs text-gray-500 md:text-right">
        Copyright © {{ new Date().getFullYear() }}<br />
        Michael Hays
      </div>
    </div>
  </div>
</template>
