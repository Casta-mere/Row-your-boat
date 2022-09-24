import App from './App'

import axios from 'axios'
import VueAxios from "vue-axios";
import Vue from 'vue'
import vuetify from './plugins/vuetify';
// #ifndef VUE3
Vue.use(VueAxios, axios)
Vue.config.productionTip = false
Vue.prototype.$axios = axios

App.mpType = 'app'
const app = new Vue({
    ...App,
    vuetify
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