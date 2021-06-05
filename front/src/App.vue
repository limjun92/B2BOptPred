<template>
  <div id="app">
    <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <fileUploadTest/>
    <fileUploadTest2/>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import fileUploadTest from './components/fileUploadTest.vue'
import fileUploadTest2 from './components/fileUploadTest2.vue'

export default {
  name: 'App',
  components: {
    HelloWorld,
    fileUploadTest,
    fileUploadTest2,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
