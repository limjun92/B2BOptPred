<template>
    <div>
        <span class ="table_tr" v-for="(label,index) in getUpload" :key='index' >
            {{label}}
        </span>
    </div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  computed:{
  ...mapGetters(["getUpload"]),
  },
}
</script>

<style>

</style>