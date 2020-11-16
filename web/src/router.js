import { createRouter, createWebHistory } from 'vue-router'

import Landing from '/src/pages/index.vue'
import Privacy from '/src/pages/privacy.vue'
import Terms from '/src/pages/terms.vue'
import Plans from '/src/pages/plans/_zip_code/index.vue'
import NotFound from '/src/pages/[not-found].vue'

const router = createRouter({
  history: createWebHistory(),
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    }

    return { top: 0, left: 0 }
  },
  routes: [
    { path: '/', component: Landing },
    { path: '/privacy', component: Privacy },
    { path: '/terms', component: Terms },
    { path: '/plans/:zip_code', component: Plans },
    { path: '/:pathMatch(.*)*', component: NotFound },
  ],
})

export default router
