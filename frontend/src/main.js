import './assets/style.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import VueAxios from 'vue-axios'
import VQrcode, { ErrorCorrectLevel, RenderOptions } from 'qrcode-vuejs';
// import VueQrcodeReader from 'vue-qrcode-reader'


const app = createApp(App)
// const pinia = createPinia()

app.use(router)
app.use(VueAxios, axios)
app.provide('axios', app.config.globalProperties.axios)
app.use(VQrcode, {
    size: 200,
    colorDark: '#000000',
    colorLight: '#ffffff',
    correctLevel: ErrorCorrectLevel.M,
    render: RenderOptions.CANVAS,
});
// app.use(VueQrcodeReader)
// app.use(pinia)
app.use(createPinia())

app.mount('#app')