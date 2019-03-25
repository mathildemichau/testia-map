<template>
    <div id="leaflet-map">
        map here
    </div>
</template>

<script>
    import L from 'leaflet';
    import 'leaflet/dist/leaflet.css';

    export default {
        data(){
            return {
                map: null,
                position: null
            }
        },
        mounted() {
            // Get the user's current location
            if(!this.position) navigator.geolocation.getCurrentPosition(this.showPosition)

            //Creation off the map by default centered on Toulouse
            this.map = L.map('leaflet-map', {
            center: [43.6044622, 1.4442469],
            zoom: 3
            });

            L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
            attribution:
                '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            }).addTo(this.map);

        },
        methods: {
            showPosition(position){
                this.position = position.coords
            },

        }
    }


    

</script>
<style>
    #leaflet-map { 
        height: 90vh; 
    }
</style>
