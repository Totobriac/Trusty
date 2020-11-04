<template>
  <div class="container" style="text-align: center">   
    <div class="my-8">
      <image-uploader
        :preview=false
        :className="['fileinput', { 'fileinput--loaded': hasImage }]"
        capture="environment"
        :debug="1"
        :maxWidth="512"
        :quality="0.9"
        doNotResize="gif"
        :autoRotate="false"
        outputFormat="verbose"
        @input="setImage"
        >   
      </image-uploader>  
    </div>    
  </div>
</template>

<script>
import mixin from "../mixin/mixin.js"
import ImageUploader from 'vue-image-upload-resize'
import { store } from "../common/store.js";

export default {
  name: "Resize",
  mixins: [mixin],
  computed:{
    storeState(){
      return store.state;
   }
  },
  data() {
    return {      
      hasImage: false,
      image: null,
      error: null,   
    }
  },
  methods: {
    /*
    Function that is triggered when a picture is selete for upload.    
    */
    setImage: function(output) {
      store.setPreloader(1)
      this.storeState.upError = "Nos ingénieurs inspectent votre photo."      
      this.image = output;
      // Check if picture as exif data
      if (this.image.exif != null) {
        // Check if picture as exif GPS data    
        if (this.image.exif.GPSLatitude) {
          // Calculate the picture CPS coordinates
          this.calculateCoordPicture()
          // Check if picture coordinates are the same as the selected restaurant       
          this.checkIfPicInRange()
          if(this.checkIfPicInRange()) {
            this.error = null
            /*
            Check if the pictures labels from Google Vison 
            do correspond with  the selected category
            */
            this.checkImageLabels()
            /*
            Convert base 64 image into jpeg format
            */                              
            this.imageConversion()                    
          } else {store.setUpError("Votre photo ne semble pas avoir été prise dans ce restaurant")
                  store.setShowCatBut()
                  store.setPreloader(0)}
        } else {store.setUpError("Avez vous activé la géolocalisation sur votre téléphone?")
                store.setShowCatBut()
                store.setPreloader(0)}
      } else {store.setUpError("Avez vous activé la géolocalisation sur votre téléphone?")
              store.setShowCatBut()
              store.setPreloader(0)}      
    },   
  },
  components: {
    ImageUploader
  }
}

</script>


<style>
#fileInput {
  display: none;
}
</style>