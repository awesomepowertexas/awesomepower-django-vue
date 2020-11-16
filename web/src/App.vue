<template>
  <app-header class="h-12 md:h-24" />

  <router-view v-slot="{ Component }" class="min-h-screen -mt-12 md:-mt-24">
    <transition name="fade" mode="out-in">
      <component :is="Component" />
    </transition>
  </router-view>

  <app-footer />
</template>

<script>
import AppHeader from '/src/components/AppHeader.vue'
import AppFooter from '/src/components/AppFooter.vue'

export default {
  name: 'App',

  components: {
    AppHeader,
    AppFooter,
  },
}
</script>
