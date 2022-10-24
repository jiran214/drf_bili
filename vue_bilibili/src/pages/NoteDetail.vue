<template>
  <div class="card" style="height:100%">
    <el-row :gutter="24" style="height:100%">

      <el-col :span="7" style="height:100%">
        <el-card class="left-card" style="height:100%">
          <div class="top" style="text-align: center;">
            <!-- 封面 -->
            <div><a :href=noteInfo.short_link>
              <el-avatar :size=120 :src=noteInfo.pic></el-avatar>
            </a></div>
          </div>
          <el-divider></el-divider>
          <div class="mid"
               style="margin-left:20px  ;flex:1;display:flex;flex-direction: column;justify-content: space-around;">
            <!-- 标题 -->
            <div><a :href=noteInfo.short_link style="text-decoration: none; color: #444;">
              <span style="font-weight:1000">{{ noteInfo.title }}</span>
            </a></div>
            <!-- 简介 -->
            <div><span>{{ '简介:' + noteInfo.desc }}</span>
              <!-- 作者 时间 分区 -->
              <div><span style="font-weight:800">{{ '作者:' + noteInfo.name }}</span>
                <el-divider direction="vertical"></el-divider>
                <span>{{ '时间:' + noteInfo.ctime }}</span>
                <span>{{ '分区:' + noteInfo.tname }}</span></div>
            </div>
            <!-- tag -->
            <div style="display:flex;">
              <el-tag v-for="(tag,index) in noteInfo.tags" :key="index" style="margin-right: 10px" type="info">
                <span>{{ tag }}</span></el-tag>
            </div>

          </div>
          <el-divider></el-divider>
          <div class="mid2" style="display:flex;flex-wrap:wrap;">
            <span>{{ '播放:' + noteInfo.view_n }} </span>
            <el-divider direction="vertical"></el-divider>
            <span>{{ '点赞:' + noteInfo.like_n }}</span>
            <el-divider direction="vertical"></el-divider>
            <span>{{ '投币:' + noteInfo.coin }}</span>
            <el-divider direction="vertical"></el-divider>
            <span>{{ '收藏:' + noteInfo.favorite }} </span>
            <el-divider direction="vertical"></el-divider>
            <span>{{ '弹幕:' + noteInfo.danmaku }}</span>
            <el-divider direction="vertical"></el-divider>
            <span>{{ '评论:' + noteInfo.reply }}</span>
            <el-divider direction="vertical"></el-divider>
            <span>{{ '分享:' + noteInfo.share }}</span>
          </div>
          <el-divider></el-divider>

          <div class="bottom" style="display:flex;flex-wrap:wrap;">
            <span>{{ '互动率:' + '50.00%' }} </span>
            <el-divider direction="vertical"></el-divider>
            <span>{{ '点赞粉播比:' + noteDetail.percent.like_n_percent }}</span>

            <span>{{ '投币粉播比:' + noteDetail.percent.coin_percent }}</span>
            <el-divider direction="vertical"></el-divider>
            <span>{{ '播放粉播比:' + noteDetail.percent.view_n_percent }}</span>

            <span>{{ '投币粉播比:' + noteDetail.percent.coin_percent }}</span>
            <el-divider direction="vertical"></el-divider>
            <span>{{ '回复粉播比:' + noteDetail.percent.reply_percent }}</span>

          </div>
          <el-divider></el-divider>


        </el-card>
      </el-col>

      <el-col :span="17" style="height:100%">
        <el-card class="right-card" style="height:100%;overflow: auto">
          <el-tabs v-model="activeName">
            <el-tab-pane label="流量分析" name="second">
              <NoteLiuLiang :noteDetail="noteDetail"></NoteLiuLiang>
              <!-- 三连变化趋势图 -->
              <!-- 互动变化趋势图 -->
            </el-tab-pane>
            <el-tab-pane label="舆情分析" name="third">评论分析</el-tab-pane>
            <!-- top10热词条形图 -->
            <!-- 词云 -->
            <!-- top10热词折线图 -->
            <!-- 词云 -->
            <!-- 评论搜索 -->
            <el-tab-pane label="标签查找" name="fifth">弹幕分析</el-tab-pane>
          </el-tabs>
        </el-card>
      </el-col>

    </el-row>
  </div>

</template>
<script>
import NoteLiuLiang from '../components/Charts/NoteLiuLiang.vue'

export default {
  name: 'NoteDetail',
  data() {
    return {
      activeName: 'second',
      id: this.$route.query.id,
      noteInfo: ''
    }
  },
  components: {
    NoteLiuLiang
  },

  mounted() {
    this.init_info()
    this.init_detail()
    this.drawChart()
  },
  methods: {
    init_info() {
      if (this.$route.query.noteInfo) {
        let noteInfo = decodeURIComponent(this.$route.query.noteInfo)
        this.noteInfo = JSON.parse(noteInfo)
      }
      console.log(this.noteInfo)
    },
    init_detail() {
      this.getRequest('/noteDetail/' + this.id).then(resp => {
        if (resp) {
          console.log(resp);
          this.$store.commit('INIT_NOTESDETAIL', resp);
        }
      })
    },

  },
  computed: {
    noteDetail() {
      return this.$store.state.noteDetail
    }
  }

}
</script>

<style scoped>

</style>