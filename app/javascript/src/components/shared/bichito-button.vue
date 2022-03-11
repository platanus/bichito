<template>
  <component
    :is="tag"
    class="p-4 text-sm font-bold text-white bg-gray-800 rounded-full sm:text-base sm:px-6 hover:shadow-lg hover:bg-gray-700"
    @click="emit('click')"
  >
    <slot />
  </component>
</template>

<script>
export default {
  computed: {
    tag() {
      if (this.alternativeTag) return this.alternativeTag;

      return this.$attrs.href ? 'a' : 'button';
    },
  },
};
</script>
