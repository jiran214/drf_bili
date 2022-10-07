<template>
  
      <el-menu
        default-active="2"
        class="el-menu-vertical-demo"
        router=true
        background-color="rgb(0, 21, 41)"
        text-color="#fff"
        active-text-color="#ffd04b">

        <el-menu-item index="/UserHome">
          <i class="el-icon-menu"></i>
          <span slot="title">UserHome</span>
        </el-menu-item>
        <el-menu-item index="/KolIndex">
          <i class="el-icon-menu"></i>
          <span slot="title">KolIndex</span>
        </el-menu-item>
        <el-menu-item index="/NoteIndex">
          <i class="el-icon-document"></i>
          <span slot="title">NoteIndex</span>
        </el-menu-item>
        <el-menu-item index="/userfav">
          <i class="el-icon-menu"></i>
          <span slot="title">UserFav</span>
        </el-menu-item>
        <el-menu-item index="/UserInfo">
          <i class="el-icon-setting"></i>
          <span slot="title">UserInfo</span>
        </el-menu-item>
      </el-menu>
  
    
</template>

<script>
export default {
  name: 'AsideNav',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
