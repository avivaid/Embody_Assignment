import Vue from 'vue'
import App from './App.vue'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import WaveSurferVue from "wavesurfer.js-vue";
import Vuetify from 'vuetify';
import 'vuetify/dist/vuetify.min.css';

Vue.use(Vuetify);
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.use(WaveSurferVue)



Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
