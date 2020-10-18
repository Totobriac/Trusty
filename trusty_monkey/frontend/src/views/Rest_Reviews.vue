<template>
  <div>
    <div class="card bg-info text-white mb-3 w-75 mt-3 mx-auto">
      <div class="card-header row ml-0 mr-0 justify-content-between">
        <div>
          <h2>{{ this.$route.params.name }}</h2>
        </div>
        <div class="row">
          <div>
            <div class="btn btn-sm btn-danger mt-2 mr-2"
                @click="showPics= !showPics
                        showCatPic()">+ 
                <i class="fa fa-camera"></i></div>
          </div>
          <div>
            <div v-show="this.$route.params.website != undefined">
              <a class="btn btn-sm btn-warning mt-2 mr-2"
                :href="this.$route.params.website"
                role="button"
                target="_blank">Site Internet</a>
            </div>
          </div>
          <div>
            <button
              @click="isHidden= !isHidden"
              class="btn btn-sm btn-success mt-2 mr-2"
            >Horaires et Accés</button>
          </div>

          <div>
            <button
              v-show="showEditor== false"
              class="btn btn-sm btn-primary mt-2 mr-2"
              @click="addRestaurant(), showTheEditor()"
            >Ajouter une Review</button>

            <button
              v-show="showEditor== true"
              class="btn btn-sm btn-danger mt-2 mr-2"
              @click="deleteReview"
            >Annuler la Review</button>
          </div>

        </div>
      </div>

      <div v-show="isHidden">
        <div class="card-body row justify-content-around">
          <div class="mt-auto">
            <ul style="list-style-type:none">
              <h3>Horaires:</h3>
              <li v-for="item in this.$route.params.opening_hours " 
                  :key="item">{{ item }}
              </li>
            </ul>
          </div>
          <div>
            <img :src="mapUrl" />
          </div>
        </div>
      </div>

      <div v-show="showPics" class="bg-muted">
        <div class="d-flex flex-row justify-content-around mb-3 ">
            <div class="mt-3" v-for="(buttonPic, index) in buttonPics" :key="buttonPic">
              <button @click="picIndex=index, showCatPic()"
                      class="btn btn-sm btn-outline-danger text-white"
              >{{ buttonPic }}
              </button>
            </div>
        </div>
      </div>

      <div class="card-footer">
        <div class="row  justify-content-around">
          <div> <i>{{ this.$route.params.adress }}</i> </div>
          <div v-show="this.$route.params.phone != undefined">
            <i class="fas fa-phone"></i> <i>{{ this.$route.params.phone }}</i>
          </div>         
        </div>   
      </div>

    </div>

    <div v-show="showPics && picByCat" class="container">
      <PicByCat :picByCat="picByCat"/>
    </div>


    <div v-if="showEditor" class="container">
      <ReviewEditor :id="review_id" />
    </div>

    <div class="container mt-3 ">
      <div class="row mt-3 reviewDetail border border-primary" 
            v-for="(review, index) in reviews" 
            :key="review.pk">
        <div class="col-8 pt-3">
          <h3>
            Visité par:
            <b>{{ review.review_author }}</b>, le
            <i>{{ review.created_at }}</i>
          </h3>
          
        </div>
        <div class="col-4 text-center my-auto">
          <button
            v-show="reviewToShow !== index"
            type="button"
            class="btn btn -sm btn-outline-info"
            @click="reviewToShow= index"
          >Consulter</button>
          <button
            v-show="reviewToShow == index"
            type="button"
            class="btn btn -sm btn-outline-danger"
            @click="reviewToShow= null"
          >Refermer</button>
        </div>      
       

        <div v-show="reviewToShow == index">
          <ReviewDetail :id="review.id" />
        </div>
      </div>
    </div>
    
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import ReviewDetail from "@/components/ReviewDetail.vue";
import ReviewEditor from "@/components/ReviewEditor.vue";
import PicByCat from "@/components/PicByCat.vue";
import { store } from "../common/store.js";
import axios from "axios"

import vueconfig from "../vueconfig.js";


export default {
  name: "rest_reviews",

  props: {
    maps: { type: String, required: true }
  },

  data() {
    return {
      isHidden: false,
      showPics: false,      
      reviewToShow: null,
      showEditor: false,
      reviews: [],
      review_id: 0,
      lat: this.$route.params.lat,
      lng: this.$route.params.lng,
      error: null,
      storeState: store.state,
      buttonPics: ['Entrée', 'Plat-principal',
                  'Dessert', 'Menu', 'Extérieur',
                  'Intérieur'],
      picIndex: null,
      picByCat: []
    }
  },

  components: {
    ReviewDetail,
    ReviewEditor,
    PicByCat
  },

  computed: {
    mapUrl() {
      const url = "https://maps.googleapis.com/maps/api/staticmap";
      const params = new URLSearchParams({
        center: `${this.$route.params.restLat},${this.$route.params.restLng}`,
        zoom: 15,
        size: "250x250",
        maptype: "terrain",
        key: "AIzaSyCGmIAISNa4W8KK24eXmH-ly_5k_vpAsos"
      });
      console.log(`${url}?${params}`)
      return `${url}?${params}`
    },
    isLoggedIn() {
      console.log(window.localStorage.getItem("username"))    
      return window.localStorage.getItem("username");      
    }  
  },
  methods: {
    
    getReviews() {
      let endpoint = `/api/rest_review/${this.maps}/`;     
      apiService(endpoint).then(data => {
        this.reviews.push(...data)       
      });
    },
    login() {
      window.localStorage.removeItem("username");         
      window.location.replace(vueconfig.baseUrl + "/accounts/login/")
    }, 

    addRestaurant() {           
      this.storeState.pictures = []
      let endpoint = `/api/restaurant/`;
      let method = "POST";
      let config = {
        maps: this.$route.params.maps,
        adress: this.$route.params.adress,
        name: this.$route.params.name,
        opened: this.$route.params.opening_hours,
        website: this.$route.params.website,
        phone: this.$route.params.phone,
        restLat: this.$route.params.restLat,
        restLng: this.$route.params.restLng   
      }        
      apiService(endpoint, method, config)
        .then(data => {
          console.log("Restaurant added!" + data);
          this.addReview();
        })
        .catch(error => console.log(error));
      },

    addReview() {      
      let endpoint = `/api/restaurant_review/`;
      let method = "POST";
      apiService(endpoint, method, {
        maps: this.$route.params.maps,
        review_author: 1
      }).then(res => {
        this.review_id = res.id;        
      })
    },

    showTheEditor() {
      this.showEditor = true
    },

    deleteReview() {
      let endpoint = `/api/restaurant_review/${this.review_id}/`;
      let method = "DELETE";
      apiService(endpoint, method);
      this.$router.push({ name: "home" });
    },

    showCatPic() {
      this.storeState.picShow = null
      this.picEndpoint = "all_single_rest_pics"
      
      if (this.picIndex == 0) {  
          this.picEndpoint = "rest_starter_pic"}      
      else if (this.picIndex == 1) {
              this.picEndpoint = "rest_main_pic"}               
      else if (this.picIndex == 2) {
              this.picEndpoint = "rest_dessert_pic"}
      else if (this.picIndex == 3) {
              this.picEndpoint = "rest_menu_pic"} 
      else if (this.picIndex== 4) {
              this.picEndpoint = "rest_outside_pic"}
      else if (this.picIndex == 5) {
              this.picEndpoint = "rest_inside_pic"}      
              
      axios.get(`${vueconfig.baseUrl}/api/${this.picEndpoint}/${this.$route.params.maps}/`)
        .then (data => {
          console.log(data.data)
          this.picByCat = data.data          
        })
    }
  },

  created() {
    this.getReviews();    
  },

  watch:{
    maps: function() {
      if (this.maps) {
        this.reviews = [];        
        this.getReviews();
      }
    }
  }
}

</script>

<style>
.naviMenu > ul li {
  list-style-type: none;
}
.reviewDetail {
  background-color: white;
  border: 1px solid b branch
}
body {
  background-image:url(../assets/Optimized-banana_palms.jpg);
}

</style>
