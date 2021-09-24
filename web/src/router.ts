import { createRouter, createWebHistory } from 'vue-router'

import Landing from '~/pages/index.vue'
import NotFound from '~/pages/[not-found].vue'
import Plans from '~/pages/plans/_zip_code/index.vue'
import Privacy from '~/pages/privacy.vue'
import Terms from '~/pages/terms.vue'

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
