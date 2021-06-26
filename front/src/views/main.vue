<template>
  <div class="home">
      <h1>home</h1>
    <signUp/>
  </div>
</template>

<script>
import signUp from '@/components/user/signUp.vue'

export default {
  name: 'Main',
  components: {
    signUp,
  },
}
</script>