<template>
  <!-- 循环卡片 -->
  <div class="list">
    <el-card v-for="(kol,index) in kols" :key="index" class="box-cards">
      <div slot="header" class="clearfix" style="display: flex;">
        <div class="left" style="">
          <!-- 头像 -->
          <div>
            <el-avatar :size=120 :src=kol.kols.face></el-avatar>
          </div>
        </div>
        <div class="mid"
             style="margin-left:20px  ;flex:1;display:flex;flex-direction: column;justify-content: space-around;">
          <!-- 名称 -->
          <div><span style="font-weight:1000">{{ kol.user_name }}</span>
            <el-divider direction="vertical"></el-divider>
            <span>{{ '用户等级:' + kol.kols.user_level }}</span></div>
          <!-- 简介 -->
          <div><span>{{ '用户编号:' + kol.kols.mid }}</span>
            <el-divider direction="vertical"></el-divider>
            <span>{{ '认证:' + kol.kols.title }}</span></div>
          <!-- 签名 -->
          <div><span>{{ '签名:' + kol.kols.sign }}</span></div>
          <!-- tag -->
          <el-tag style="width:45%" type="info">标签</el-tag>
        </div>
        <div class="right" style="display: flex;flex-direction: column;align-items: center;">
          <el-button plain style="width: 100px;margin-top: 20px;" type="danger">取消收藏</el-button>
          <el-button plain style="width: 100px;margin-right: 10px;margin-top: 15px;" type="danger">查看详情</el-button>
        </div>
      </div>
      <div class="text item" style="display:flex;justify-content: space-around;">
        <span>{{ '粉丝量:' + kol.kols.follower }} </span>
        <el-divider direction="vertical"></el-divider>
        <span>{{ '播放量:' + kol.kols.play_view }}</span>
        <el-divider direction="vertical"></el-divider>
        <span>{{ '获赞量:' + kol.kols.likes }}</span>
      </div>
    </el-card>
  </div>

</template>

<script>
export default {
  name: 'KolCard',
  computed: {
    kols() {
      console.log(this.$store.state.kols)
      return this.$store.state.kols

    },
  },
  props: {
    //接收父组件传过来的值
    kol: Object,
    msg: String
  },
  mounted() {
    this.getRequest('/kolfav').then(resp => {
      if (resp) {
        console.log(resp);
        this.$store.commit('INIT_KOLFAVS', resp);
        this.total = resp.data.count
      }
    })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.box-cards {
  margin-bottom: 25px;
}


</style>
