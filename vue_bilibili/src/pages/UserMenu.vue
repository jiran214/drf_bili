<template>
  <div class="homeWrap">
    <el-container>
    <el-aside width="200px"><AsideNav></AsideNav></el-aside>
    <el-container>
      <el-header><HomeHeader class="header"></HomeHeader></el-header>
      <el-main><router-view></router-view></el-main>
      <el-footer>Footer</el-footer>
    </el-container>
  </el-container>
  </div>
  
  
  
</template>
<script>
import AsideNav from '../components/AsideNav'
import HomeHeader from '../components/HomeHeader'

export default {
    name: 'UserMenu',
    data() {
      return {
        
      }
    },
    components: {
      AsideNav,
      HomeHeader
    }
}
</script>

<style scoped>
  .el-header{
    background-color: #dcd8d8;
    padding: 0px;

    margin: 0px;
    height: 100%;
  }

  header{
    padding: 0 ;
  } 

  .el-main,.el-footer {
    background-color: #E9EEF3;
    color: #333;
    /* text-align: center; */
  }

  .el-aside {
    background-color:rgb(0, 21, 41);
    color: #333;
    line-height: 500%;
  }

  .homeWrap{
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
  }

  .el-container{
    padding: 0px;

    margin: 0px;
    height: 100%;
  } 
</style>