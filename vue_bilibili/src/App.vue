<template>
  <div id="app">
    <UserHome></UserHome>

  </div>
</template>

<script>
import UserHome from './pages/UserMenu.vue'

export default {
  name: 'App',
  components: {
    UserHome
    
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;

}
</style>
