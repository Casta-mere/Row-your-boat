import App from './App'


import axios from 'axios'
import VueAxios from "vue-axios";

Vue.use(VueAxios, axios)

// #ifndef VUE3
import Vue from 'vue'
Vue.config.productionTip = false
Vue.prototype.$axios = axios

App.mpType = 'app'
const app = new Vue({
    ...App
})
app.$mount()
    // #endif

// #ifdef VUE3
import { createSSRApp } from 'vue'
export function createApp() {
    const app = createSSRApp(App)
    return {
        app
    }
}


// #endif