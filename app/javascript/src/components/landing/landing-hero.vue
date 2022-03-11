<template>
  <section>
    <div class="container flex flex-col items-center px-8 mx-auto mt-28">
      <div class="flex flex-col items-center sm:w-7/12 xl:w-6/12">
        <h1 class="text-xl font-semibold text-center text-gray-800 md:text-2xl lg:text-4xl">
          Curso de programación para estudiantes de enseñanza media
        </h1>
      </div>
      <inline-svg
        :src="require('../../../../assets/images/bee-path.svg')"
        class="absolute left-0 w-11/12 fill-current md:w-10/12 md:left-10 top-16 md:top-24"
      />
      <img
        :src="require('../../../../assets/images/landing-code.png')"
        class="absolute w-7/12 sm:w-7/12 md:w-6/12 top-52"
      >
      <div class="mt-40 sm:mt-56 md:mt-64 lg:mt-80 xl:mt-96">
        <bichito-button>
          Conoce más del programa
        </bichito-button>
      </div>
    </div>
  </section>
</template>

<script>
import BichitoButton from '../shared/bichito-button.vue';

export default {
  components: { BichitoButton },
};
</script>
