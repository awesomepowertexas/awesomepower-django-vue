<template>
  <div id="header" class="flex items-end px-5 md:px-12">
    <div
      class="z-20 w-full max-w-6xl flex items-center justify-between mx-auto"
    >
      <nuxt-link to="/">
        <svg-logo id="header-logo" class="w-48 md:w-80" />
      </nuxt-link>

      <span
        class="cursor-pointer font-bold text-sm hover:text-blue-700 mb-1"
        @click="navigateToFaqs"
      >
        FAQs
      </span>
    </div>
  </div>
</template>

<script>
import SvgLogo from '../assets/svg/logo.svg'

export default {
  components: {
    SvgLogo,
  },

  methods: {
    navigateToFaqs() {
      if (this.$route.name === 'index') {
        document.getElementById('faqs').scrollIntoView({ behavior: 'smooth' })
      } else {
        this.$router.push({ path: '/', hash: '#faqs' })
      }
    },
  },
}
</script>

<style scoped lang="postcss">
#header-logo:hover > path:nth-child(3) {
  fill: hsl(207, 90%, 96%);
}
</style>
