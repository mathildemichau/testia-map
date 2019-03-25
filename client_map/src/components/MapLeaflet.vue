<template>
  <div id="leaflet-map"></div>
</template>

<script>
import L from "leaflet";
import "leaflet/dist/leaflet.css";

export default {
  data() {
    return {
      map: null,
      position: null,
    };
  },
  mounted() {


    //Creation of the map by default centered on Toulouse
    this.map = L.map("leaflet-map", {
      center: [43.6044622, 1.4442469],
      zoom: 2
    });

    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
      attribution:
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(this.map);

    this.map.on("click", this.addMarker);
  },
  methods: {
    addMarker(e) {
      let popup = L.popup();
      popup.setLatLng(e.latlng).openOn(this.map);

      this.$emit("newMarker", {latitude: e.latlng.lat, longitude: e.latlng.lng})
    }
  }
};
</script>
<style>
#leaflet-map {
  height: 80vh;
}
.leaflet-popup-content-wrapper {
  background: no-repeat url("../assets/logoTestia.jpg") ;
  height: 35px;
  width: 145px;
}
</style>
