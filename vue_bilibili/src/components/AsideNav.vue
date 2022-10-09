<template>
  
      <el-menu
          default-active="2"
          class="el-menu-vertical-demo"
          router=true
          background-color="rgb(0, 21, 41)"
          text-color="#fff"
          active-text-color="#ffd04b">
        <!-- <el-menu-item index="/UserHome"> -->
        <el-image :src='logo' fit="contain" style="padding-top:10px"></el-image>
        <!-- </el-menu-item> -->
        <el-menu-item index="/UserHome">
          <i class="el-icon-menu"></i>
          <span slot="title">主页</span>
        </el-menu-item>
        <el-menu-item index="/KolIndex">
          <i class="el-icon-s-custom"></i>
          <span slot="title">UP主搜索</span>
        </el-menu-item>
        <el-menu-item index="/NoteIndex">
          <i class="el-icon-document"></i>
          <span slot="title">素材搜索</span>
        </el-menu-item>
        <el-menu-item index="/userfav">
          <i class="el-icon-star-on"></i>
          <span slot="title">我的收藏</span>
        </el-menu-item>
        <el-menu-item index="/UserInfo">
          <i class="el-icon-user-solid"></i>
          <span slot="title">个人信息</span>
        </el-menu-item>
      </el-menu>
  
    
</template>

<script>
export default {
  name: 'AsideNav',
  data() {
    return {
      logo: "http://localhost:5000/media/logo/sec_logo.png"
    }
  },
  props: {
    msg: String
  },
  mounted() {
    // this.init_logo()
  },
  methods: {
    init_logo() {

    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
