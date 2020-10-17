<template>
  <div class="home">
    <div class="container mt-3">      
      <div class="row mt-3 singleReview border border-primary"
            v-for="(review, index) in reviews"
            :key="review.pk">
        <div class="col-8">
          <p class="mb-0">Visité par:
            <span><b class="text-danger">{{ review.review_author }}</b>, le  <i>{{ review.created_at }}</i></span>
          </p>
          <h2 @click="getDetails(review.maps)" class="restName"><b> {{ review.restaurant_name }}</b></h2>                      
          <p class="text-success" >{{ review.restaurant_adress }}</p> 
          <hr class="mb-0">    
        </div>
        <div class="col-4 text-center my-auto">
          <button v-show="reviewToShow !== index" 
                  type="button" class="btn btn -sm btn-outline-info" 
                  @click="reviewToShow= index">Consulter
          </button>
          <button v-show="reviewToShow == index" 
                  type="button" class="btn btn -sm btn-outline-danger" 
                  @click="reviewToShow= null">Refermer
          </button>  
        </div>       
        <hr>

         <div v-show="reviewToShow == index">
          <ReviewDetail
          :id="review.id"/>
        </div>       
        
      </div>

    <div class="mt-3">          
          <button
          v-show="next"
          @click="getReviews"
          class="loadBtn btn btn btn-outline-info"
          >Charger Plus
          </button>
    </div>

    </div>

  </div>  
</template>

<script>
import { apiService } from "@/common/api.service.js";
import ReviewDetail from "@/components/ReviewDetail.vue";

export default {
  name: "home",
  data () {
    return {
      reviews: [],
      reviewToShow: null,
      apiKey: "AIzaSyCGmIAISNa4W8KK24eXmH-ly_5k_vpAsos",
      next: null,
    }
  },
  components: {
    ReviewDetail
  },
  methods: {
    getReviews() {      
      let endpoint = "/api/restaurant_review/";
      if (this.next) {
        endpoint = this.next
      }
      apiService(endpoint)
        .then(data => {          
          this.reviews.push(...data.results)
          if (data.next){
            this.next = data.next
          } else {
            this.next = null
          }
      })
    },
    getDetails(maps) {
      let endpoint = `/api/restaurant/${maps}/`
      apiService(endpoint)
        .then(resp=> {
          console.log(resp)
          this.$router.push({ name: "rest_reviews", 
                  params: { maps: resp.maps,
                            name: resp.name,
                            adress: resp.adress,                          
                            opening_hours: resp.opened,
                            phone: resp.phone,
                            website: resp.website,                            
                            restLat: resp.restLat,
                            restLng: resp.restLng}}) 
        })
    }
  },
    mounted() {      
      this.getReviews()
      console.log(this.reviews) 
      },
};
</script>

<style >
.pac-container:after {  
  background-image: none !important;
    height: 0px;
}
body {
  background-image:url(../assets/Optimized-117.jpg);
}
.singleReview {
  background-color: white;
  border: 1px solid 
}
a:hover {
  text-decoration: none;
}
.loadBtn {
  background-color: white;
}
.restName:hover {
  cursor: pointer;
}
</style>