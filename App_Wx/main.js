import App from './App'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import axios from 'axios'
import VueAxios from "vue-axios";
import Vue from 'vue'
import vuetify from './plugins/vuetify';
// #ifndef VUE3
Vue.use(VueAxios, axios, ElementUI)
Vue.config.productionTip = false
Vue.prototype.$axios = axios

App.mpType = 'app'
const app = new Vue({
    ...App,
    vuetify,
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