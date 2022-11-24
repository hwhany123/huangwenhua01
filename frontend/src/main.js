import {createApp} from 'vue'
import App from './App.vue'
import router from './router'
//import ElementUI from 'element-ui'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
//import 'element-ui/lib/theme-chalk/index.css';
import * as ElementPlusIconsVue from '@element-plus/icons-vue'



URLSearchParams.prototype.appendIfExists = function (key, value) {
    if (value !== null && value !== undefined) {
        this.append(key, value)
    }
};

const AP1=createApp(App)
AP1.use(router)
//AP1.use(ElementUI)
AP1.use(ElementPlus)

for (const [key, component] of Object.entries(ElementPlusIconsVue)) {AP1.component(key, component)}
AP1.mount('#app')