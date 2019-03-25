<template>
  <div id="app">
    <map-leaflet/>
  </div>
</template>

<script>
import MapLeaflet from './components/MapLeaflet.vue'

export default {
  name: 'app',
  components: {
    MapLeaflet
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
