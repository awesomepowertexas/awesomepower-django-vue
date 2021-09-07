<script setup>
import AppFooter from '~/components/_layouts/AppFooter.vue'
import AppHeader from '~/components/_layouts/AppHeader.vue'
</script>

<template>
  <AppHeader class="h-12 md:h-24" />

  <router-view v-slot="{ Component }" class="min-h-screen -mt-12 md:-mt-24">
    <Transition name="fade" mode="out-in">
      <Component :is="Component" />
    </Transition>
  </router-view>

  <AppFooter />
</template>
