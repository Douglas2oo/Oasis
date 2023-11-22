
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import 'element-plus/dist/index.css'
import ElementPlus from 'element-plus'
import axios from 'axios'
import App from './App.vue'
import router from './router'
import store from './stores'



const app = createApp(App)

app.config.globalProperties.$axios = axios
app.use(createPinia())
app.use(router)
app.use(ElementPlus)
app.use(store)
app.mount('#app')
