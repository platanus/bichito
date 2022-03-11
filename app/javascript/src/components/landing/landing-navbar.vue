<template>
  <nav
    class="absolute top-0 left-0 right-0 z-10 items-center py-5"
    :class="isMenuOpen ? 'bg-sc-gray-darker': 'bg-sc-blue' "
  >
    <inline-svg
      :src="require('../../../../assets/images/icons/bichito.svg')"
      class="text-gray-700 w-24 lg:w-32 mx-10 md:mx-32 lg:mx-56"
      alt="Logo Bichito"
    />
  </nav>
</template>

<script>
export default {
};
</script>