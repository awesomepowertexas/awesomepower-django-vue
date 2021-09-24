<script setup lang="ts">
import FAQs from '~/components/Landing/FAQs.vue'
import ViewPlans from '~/components/Landing/ViewPlans.vue'
import { onMounted } from 'vue'
import { useHead } from '@vueuse/head'
import { useRoute } from 'vue-router'

useHead({ title: 'Find a cheap electricity plan, headache free' })

const route = useRoute()

onMounted(() => {
  if (route.hash === '#faqs') {
    setTimeout(() => {
      document.getElementById('faqs')?.scrollIntoView({ behavior: 'smooth' })
    })
  }
})
</script>

<template>
  <div class="relative">
    <img
      src="/src/assets/svg/intro-bg-mobile.svg"
      class="absolute md:hidden z-[-10] w-screen h-screen top-0 left-0"
    />

    <img
      src="/src/assets/svg/intro-bg.svg"
      class="absolute hidden md:block z-[-10] w-screen h-screen top-0 left-0"
    />

    <img
      src="/src/assets/svg/pawprints-mobile.svg"
      class="z-[-10] absolute md:hidden w-screen left-0 top-[65vh]"
    />

    <div
      class="z-[-10] absolute hidden md:block w-screen left-0 top-[calc(80vh-40vw)] max-h-full overflow-hidden"
    >
      <img src="/src/assets/svg/pawprints.svg" />
    </div>

    <div id="intro-section" class="h-screen p-4 pt-[16vh] md:pt-[20vh]">
      <h1
        class="font-bold font-solway text-3xl text-center md:text-5xl md:leading-tight"
      >
        <div>
          Find a cheap
          <br class="md:hidden" />
          electricity plan,
        </div>

        <div>
          <span class="border-b-4 border-blue-300 px-3 pb-1">
            headache-free</span
          >
        </div>
      </h1>

      <ViewPlans class="mx-auto mt-16 md:mt-20" />
    </div>

    <FAQs />
  </div>
</template>
