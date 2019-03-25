<template>
  <div>
    <h2>Cliquez sur un pays</h2>
    <p v-if="distance">Situé à {{distance}} km de distance</p>
    <img v-if="country" :src="src">
  </div>
</template>
<script>
export default {
  props: {
    country: String,
    distance: Number
  },
  computed: {
    src() {
      //Get flags with countryflags site
      return `https://www.countryflags.io/${this.country}/flat/64.png`;
    }
  }
};
</script>

<style scoped>
div {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
</style>



