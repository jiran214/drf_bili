import Vue from 'vue'
import App from './App.vue'

import router from './router'
import store from './store'

import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import {postRequest} from "@/utils/api";
import {putRequest} from "@/utils/api";
import {getRequest} from "@/utils/api";
import {deleteRequest} from "@/utils/api";
//引入echarts
// import echarts from 'echarts'
import * as echarts from "echarts";
//vue全局注入echarts
Vue.prototype.$echarts = echarts;
Vue.use(ElementUI)
Vue.config.productionTip = false
// 插件形式使用请求
Vue.prototype.postRequest = postRequest
Vue.prototype.putRequest = putRequest
Vue.prototype.getRequest = getRequest
Vue.prototype.deleteRequest = deleteRequest

new Vue({
    render: h => h(App),
  store,
  router,

}).$mount('#app')
