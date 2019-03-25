<template>
  <div id="app">
    <show-location/>
    <map-leaflet @newMarker="updateMarker" @newPosition="updatePosition"/>
  </div>
</template>

<script>
import MapLeaflet from "./components/MapLeaflet.vue";
import ShowLocation from "./components/ShowLocation.vue";

export default {
  name: "app",
  components: {
    MapLeaflet,
    ShowLocation
  },
  data() {
    return {
      position: null,
      distance: null,
      markerPosition: null,
      country: null
    };
  },
  methods: {
    updateMarker(coords) {
      this.markerPosition = coords;
      if(this.position) this.distance = this.getDistance(this.position, this.markerPosition);
      this.getCountry();
    },
    updatePosition(coords) {
      this.position = coords;
    },
    //Calculates distance between 2 points
    getDistance(p1, p2) {
      //Calculates radius of a value
      const rad = x => (x * Math.PI) / 180;

      const R = 6378137; // Earth’s mean radius in meter
      const dLat = rad(p2.latitude - p1.latitude);
      const dLong = rad(p2.longitude - p1.longitude);
      let a =
        Math.sin(dLat / 2) * Math.sin(dLat / 2) +
        Math.cos(rad(p1.latitude)) *
          Math.cos(rad(p2.latitude)) *
          Math.sin(dLong / 2) *
          Math.sin(dLong / 2);
      let c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
      let d = (R * c) / 1000;
      return d.toFixed(2);
    },
    rad(x) {
      return;
    },
    async getCountry() {
      let res = await fetch(`http://api.geonames.org/countrySubdivisionJSON?lat=${this.markerPosition.latitude}&lng=${this.markerPosition.longitude}&username=mathildemichau`)
      let json = await res.json()
      this.country = json.countryName
    }
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
