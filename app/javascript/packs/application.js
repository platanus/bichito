import Vue from 'vue/dist/vue.esm';
import InlineSvg from 'vue-inline-svg';
import '../css/application.css';


Vue.component('inline-svg', InlineSvg);

document.addEventListener('DOMContentLoaded', () => {
  const app = new Vue({
    el: '#vue-app',
    components: { App },
  });

  return app;
});
