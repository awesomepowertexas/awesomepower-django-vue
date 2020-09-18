<template>
  <div>
    <app-header class="h-12 md:h-24" />

    <nuxt class="min-h-screen -mt-12 md:-mt-24" />

    <app-footer />
  </div>
</template>

<script>
import AppHeader from '@/components/AppHeader'
import AppFooter from '@/components/AppFooter'

export default {
  components: {
    AppHeader,
    AppFooter,
  },
}
</script>
