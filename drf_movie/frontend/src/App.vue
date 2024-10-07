<template>
  <router-view/>
</template>

<script>
import axios from 'axios';
export default{
  name:'App',
  beforeCreate(){
    this.$store.commit('initializeStore')
  },
}
</script>


