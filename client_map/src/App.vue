<template>
  <div id="app">
    <show-location :country="country" :distance="distance"/>
    <map-leaflet @newMarker="updateMarker" :marker="markerPosition" v-if="markerPosition"/>
  </div>
</template>

<script>
import MapLeaflet from "./components/MapLeaflet.vue";
import ShowLocation from "./components/ShowLocation.vue";
import dateFormat from "dateformat";
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
      country: null,
      markerPosition: null,
      ip: null
    };
  },
  methods: {
    updateMarker(coords) {
      this.markerPosition = coords;
      if (this.position)
        this.distance = this.getDistance(this.position, this.markerPosition);
      this.getCountry();
      this.storePosition(this.markerPosition);
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
      return Number(d.toFixed(2));
    },
    //Store position for each time of the marker position
    storePosition(newPosition) {
      console.log("post", newPosition);
      let dataToStore = {
        ip: this.ip,
        location: JSON.stringify(newPosition)
      };
      fetch("http://localhost:8000/maprequests/", {
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json"
        },
        body: JSON.stringify(dataToStore)
      })
        .then(res => res.json())
        .then("post", console.log)
        .catch(console.error);
    },
    //Get country with API geonames
    async getCountry() {
      let res = await fetch(
        `http://api.geonames.org/countrySubdivisionJSON?lat=${
          this.markerPosition.latitude
        }&lng=${this.markerPosition.longitude}&username=mathildemichau`
      );
      let json = await res.json();
      this.country = json.countryCode;
    }
  },
  mounted() {
    // Get the user's current location
    navigator.geolocation.getCurrentPosition(position => {
      this.position = position.coords;
      this.distance = this.getDistance(this.position, this.markerPosition);
    });

    //Get users's IP address with http://www.geoplugin.net
    fetch("http://www.geoplugin.net/json.gp")
      .then(res => res.json())
      .then(json => (this.ip = json.geoplugin_request))
      .catch(console.error);

    //Get the last location stored
    fetch("http://localhost:8000/maprequests/")
      .then(res => res.json())
      .then(json => {
        let data = JSON.parse(json.pop().location);
        if (data) {
          this.markerPosition = data;
          this.getCountry();
        }
      })
      .catch(console.error);
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
  width: 90%;
  margin: 0 auto;
}
</style>
