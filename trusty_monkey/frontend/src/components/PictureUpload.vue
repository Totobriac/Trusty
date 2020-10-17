<template>
  <div>
    <div class="row">
      <div v-for="(picture, index) in storeState.pictures"
          :key="index"
          class="col-md-2 my-auto mt-2">   
          <div >                 
            <img class="img-thumbnail img-responsive" 
                :src="picture.url">
                <button class='btn btn-sm'
                @click="deleteMe(picture, picToDelete = index)">
                <i class="far fa-minus-square fa-2x text-danger"></i>
                </button>                           
          </div>          
      </div>      
    </div>    
	</div>
</template>

<script>
import { store } from "../common/store.js"
import { apiService } from "@/common/api.service.js";

export default {
  name:"PictureUpload",
  data () {
    return {
      picToDelete: null,
    }
  },
  computed:{
    storeState(){
      return store.state;
   }
  },
  methods: {
    deleteMe(picture) {     
      let endpoint = picture.apiUrl + picture.id +"/"
      let method = "DELETE";
      apiService(endpoint, method);      
      store.deletePicture(this.picToDelete)      
    }
  }
}
</script>
