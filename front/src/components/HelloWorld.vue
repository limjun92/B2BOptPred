<template>
  <div class="hello">
    <h1>Hello World</h1>
    <table border = "1">
      <th>이름</th>
      <th>별명</th>
      <th>팀</th>
      <tr class ="table_tr" v-for="(User,index) in getUserList" :key='index' >
        <td>{{User.usersName}} </td>
        <td>{{User.usersNickname}}</td>
        <td>{{User.usersTel}}</td>
      </tr>
    </table>
    
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  
  name: 'HelloWorld',
  // props: {
  //   msg: String
  // },
  computed:{
    ...mapGetters(["getUserList"]),
  },
  methods:{
      getUser(){
          console.log("??")
          console.log(this.getUserList)
      }
  },
  mounted(){
    this.$store.dispatch('loadUserList');
  },
  watch:{
      getUserList:function(){
          this.getUser();
      }
  }
  
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
/* h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
} */
</style>
