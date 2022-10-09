<template>
  <!-- 循环卡片 -->
  <div class="list">
    <el-card v-for="(note,index) in this.$store.state.notes" :key="index" class="box-cards">
      <div slot="header" class="clearfix" style="display: flex;">
        <div class="left" style="">
          <!-- 封面 -->
          <div><a :href=note.notes.short_link>
            <el-avatar :size=120 :src=note.notes.pic></el-avatar>
          </a></div>
        </div>
        <div class="mid"
             style="margin-left:20px  ;flex:1;display:flex;flex-direction: column;justify-content: space-around;">
          <!-- 标题 -->
          <div><a :href=note.notes.short_link style="text-decoration: none; color: #444;">
            <span style="font-weight:1000">{{ note.notes.title }}</span>
          </a></div>
          <!-- 简介 -->
          <div><span>{{ '简介:' + note.notes.des }}</span>
            <!-- 作者 时间 分区 -->
            <div><span style="font-weight:800">{{ '作者:' + note.notes.name }}</span>
              <el-divider direction="vertical"></el-divider>
              <span>{{ '时间:' + note.notes.ctime }}</span>
              <el-divider direction="vertical"></el-divider>
              <span>{{ '分区:' + note.notes.tname }}</span></div>
          </div>
          <!-- tag -->
          <el-tag style="width:45%" type="info"><span>{{ 'tag:' + note.tag }}</span></el-tag>

        </div>
        <div class="right" style="display: flex;flex-direction: column;align-items: center;">
          <el-button plain style="width: 100px;margin-top: 20px;" type="danger">取消收藏</el-button>
          <el-button plain style="width: 100px;margin-right: 10px;margin-top: 15px;" type="danger">查看详情</el-button>
        </div>
      </div>
      <div class="text item" style="display:flex;justify-content: space-around;">
        <span>{{ '播放:' + note.notes.view_n }} </span>
        <el-divider direction="vertical"></el-divider>
        <span>{{ '点赞:' + note.notes.like_n }}</span>
        <el-divider direction="vertical"></el-divider>
        <span>{{ '投币:' + note.notes.coin }}</span>
        <el-divider direction="vertical"></el-divider>
        <span>{{ '收藏:' + note.notes.favorite }} </span>
        <el-divider direction="vertical"></el-divider>
        <span>{{ '弹幕:' + note.notes.danmaku }}</span>
        <el-divider direction="vertical"></el-divider>
        <span>{{ '评论:' + note.notes.reply }}</span>
        <el-divider direction="vertical"></el-divider>
        <span>{{ '分享:' + note.notes.share }}</span>
      </div>
    </el-card>
  </div>

</template>

<script>
export default {
  name: 'NoteCard',
  computed: {
    // kols() {
    //   return this.$store.state.notes
    // },
  },
  props: {
    //接收父组件传过来的值

  },
  mounted() {
    this.getRequest('/notefav').then(resp => {
      if (resp) {
        console.log(resp);
        this.$store.commit('INIT_NOTEFAVS', resp);
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
