<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light my-navbar">
    <div class="container">
      <router-link :to="{ name: 'home' }" class="navbar-brand">TrustyMonkey</router-link>

      <div class="collapse navbar-collapse flex-row justify-content-end">

        <vue-google-autocomplete
          ref="inputField"
          id="map"
          class="form-control mr-sm-2"
          placeholder="Rechercher un restaurant"
          v-on:placechanged="getAddressData"
          country="fr"
          types="establishment"          
        ></vue-google-autocomplete>

        <ul class="navbar-nav mr-2">
          <li class="nav-item active">
            <a v-if="isLoggedIn" class="outBtn btn btn-outline-danger" v-on:click="logout">Se deconnecter</a>
            <a v-else class="inBtn btn btn-outline-primary" v-on:click="login" >Se connecter</a>
          </li>
        </ul>

      </div>
    </div>
  </nav>
</template>


<script>
import VueGoogleAutocomplete from "vue-google-autocomplete";
import { store } from "../common/store.js";
import vueconfig from "../vueconfig.js";

const baseUrl = vueconfig.baseUrl;

export default {
  name: "NavbarComponent",
  components: { VueGoogleAutocomplete },
  data() {
    return {
      requestUser: false,
      addressData: "",            
    };
  },
  computed: {
    isLoggedIn() {
      console.log(window.localStorage.getItem("username"))    
      return window.localStorage.getItem("username");      
    }
  },   
  methods: {
    login() {
      window.localStorage.setItem("username", "toto")     
      window.location.replace(baseUrl + "/accounts/login/")
    },
    logout() {
      window.localStorage.removeItem("username");         
      window.location.replace(baseUrl + "/accounts/logout/")
    },   
    getAddressData(addressData, placeResultData) {
      this.placeResultData = placeResultData;
      console.log(this.placeResultData)    
      this.lat = this.placeResultData.geometry.location.lat(),
      this.lng = this.placeResultData.geometry.location.lng(),        
      store.setRestLat(this.lat)      
      store.setRestLng(this.lng)
      
      if (this.placeResultData.types.includes('restaurant') ||
          this.placeResultData.types.includes('bar') ) 
        { if (this.placeResultData.opening_hours == undefined) {        
          this.opening_hours = ["lundi: Non renseigné", "mardi: Non renseigné", 
                                "mercredi: Non renseigné", "jeudi: Non renseigné",
                                "vendredi: Non renseigné", "samedi: Non renseigné",
                                "dimanche: Non renseigné"] 
        } else { this.opening_hours = this.placeResultData.opening_hours.weekday_text}

        this.$router.push({ name: "rest_reviews", 
                  params: { maps: this.placeResultData.place_id,
                            name: this.placeResultData.name,
                            adress: this.placeResultData.formatted_address,                          
                            opening_hours: this.opening_hours,
                            phone: this.placeResultData.formatted_phone_number,
                            website: this.placeResultData.website,
                            type: this.placeResultData.types,
                            restLat: this.lat,
                            restLng: this.lng}})      
        this.$refs.inputField.$refs.autocomplete.value='';   

      } else { this.$router.push({ name: "notarest" });
              this.$refs.inputField.$refs.autocomplete.value='';}
    }
  }
}
</script>

<style scoped>
.my-navbar {
  border-bottom: 1px solid grey;
}
.navbar-brand {
  font-weight: bold;
  font-size: 200%;
}
.navbar-brand:hover {
  color: grey !important;
}
#map {
  width: 45%;
}
.form-control {
  border-left: none;
  border-right: none;
  border-top: none;
  border-bottom: 1px solid lightblue;
}
.outBtn {
  color: red;
}
.outBtn:hover {
  color: white;
}
.inBtn {
  color: blue;
}
.inBtn:hover {
  color: white;
}
</style>
