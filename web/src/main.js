import './index.css'
import App from './App.vue'
import { createApp } from 'vue'
import { createHead } from '@vueuse/head'
import router from './router'

const app = createApp(App)
const head = createHead()

app.use(router)
app.use(head)

app.mount('#app')
