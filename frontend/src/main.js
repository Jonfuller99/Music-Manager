import { createApp } from 'vue'
import { createPinia } from 'pinia'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'



import App from './App.vue'
import router from './router'
import './assets/main.css'

import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faDownload, faArrowRight, faRotateRight } from '@fortawesome/free-solid-svg-icons'

library.add(faDownload, faArrowRight, faRotateRight)


const app = createApp(App)

const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)

app.use(pinia)
app.use(router)

app.component('font-awesome-icon', FontAwesomeIcon)

app.mount('#app')