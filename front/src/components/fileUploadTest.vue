<template>
  <div>
    <h1>fileUploadTest</h1>
      <input type="file" id="files" ref="files" v-on:change="handleFileUpload()" multiple />
      <button v-on:click="submitFile()">Submit</button>
  </div>
</template>

<script>
import axios from 'axios';
let api_url = process.env.VUE_APP_APIURL + "/file";

export default {
  methods: {
    submitFile() {
      for (var i = 0; i < this.files.length; i++) {
          let formData = new FormData();
          formData.append('title', this.title);
          formData.append('files', this.files[i]);
          if(i<5){
            console.log(this.files[i])
          }
          axios.post(api_url + '/upload',
              formData, {
                  headers: {
                      'Content-Type': 'multipart/form-data'
                  }
              }
              ).then(function(res) {
                  console.log(res.data[0])
                  console.log('SUCCESS!!');
              })
              .catch(function() {
                  console.log('FAILURE!!');
              });
      }
    },
      handleFileUpload() {
        this.files = this.$refs.files.files;
        console.log(this.files);
      }
    }
  }
</script>

<style>

</style>