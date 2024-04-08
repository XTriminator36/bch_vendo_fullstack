import './assets/style.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import VueAxios from 'vue-axios'
// import VueQrcodeReader from 'vue-qrcode-reader'


const app = createApp(App)
app.use(router)
app.use(VueAxios, axios)
app.provide('axios', app.config.globalProperties.axios)
// app.use(VueQrcodeReader)
app.mount('#app')

