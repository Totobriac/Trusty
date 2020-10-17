<template>
  <div>
    <div class="row flex mt-4">

      <div class="col-md-6">
        <div class="row" id="grid">
          <div v-for="(picture, index) in pictures"
          :key="picture.pk"
          class="col-md-3 my-auto"
          >   
          <div @click="picToShow= index">                 
            <img class="img-thumbnail img-responsive" :src="picture.picture_1">
          </div>
          </div>  
        </div>
      </div>

      <div class="col-6 d-flex align-items-center justify-content-center" style="width:450px; height:450px;">        
          <div v-if="picToShow!==null">                    
             <img :src="pictures[picToShow].picture_1" 
                  class="img-responsive" 
                  style="width:auto; height:auto; max-width:450px; max-height:450px;"
                  />   
          </div>    
      </div>
      
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  name: "ReviewDetail",
  data () {
    return {      
      pictures: [],
      picToShow: null,
      fullWidthImage: false               
    }
  },
  props: {
    id: {
      type: Number,
      required: true
    }
  },
  methods: {
    getPictures() {
      let endpoint = `/api/every_review_pics/${this.id}/`;            
      apiService(endpoint)        
        .then(data => {          
          this.pictures.push(...data)                   
      })      
     },    
  },  
  created() {      
    this.getPictures()     
  } 
};
</script>

<style>
.full {
  width: 100%;
  height: auto;
}
img:hover {
  cursor: pointer;
}
</style>