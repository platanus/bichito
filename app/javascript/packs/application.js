import Vue from 'vue/dist/vue.esm';
import InlineSvg from 'vue-inline-svg';
import '../css/application.css';

import LandingHero from '../src/components/landing/landing-hero.vue';
import LandingNavbar from '../src/components/landing/landing-navbar.vue';

Vue.component('inline-svg', InlineSvg);

document.addEventListener('DOMContentLoaded', () => {
  const app = new Vue({
    el: '#vue-app',
    components: {
      LandingHero,
      LandingNavbar,
    components: { App },
    },
  });

  return app;
});
