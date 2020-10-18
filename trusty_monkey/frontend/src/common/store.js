export const store = {
    state: {      
      pictures: [],
      labels: [],
      restLat: null,
      restLng: null,
      file: null,      
      showCatBut: true,
      upError: null,
      preLoader: null,
      picShow: null,
    },
    addPicture(newPicture) {      
      this.state.pictures.push(newPicture);
    },
    deletePicture(index) {
      this.state.pictures.splice(index,1);
    },
    setRestLat(lat) {
      this.state.restLat = lat
    },
    setRestLng(lng) {
      this.state.restLng = lng
    },
    setFile(file) {
      this.state.file = file
    },   
    addLabels(label) {
      this.state.labels.push(label)
    },
    setShowCatBut() {
      this.state.showCatBut = !this.state.showCatBut
    },
    setUpError(error) {
      this.state.upError = error 
    },
    setPreloader(int) {
      this.state.preLoader = int
    },
    setPicShow(index) {
      this.state.picShow = index
    }
  }