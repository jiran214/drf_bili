<template>
  <div class="card" style="height:100%">
    <el-row :gutter="24" style="height:100%">

      <el-col :span="7" style="height:100%">
        <el-card class="left-card" style="height:100%">
          <div class="top" style="">
            <!-- 头像 -->
            <div>
              <el-avatar :size=120 :src=kolInfo.face></el-avatar>
            </div>
          </div>
          <div class="mid"
               style="margin-left:20px  ;flex:1;display:flex;flex-direction: column;justify-content: space-around;">
            <!-- 名称 -->
            <div><span style="font-weight:1000">{{ kolInfo.user_name }}</span>
              <el-divider direction="vertical"></el-divider>
              <span>{{ '用户等级:' + kolInfo.user_level }}</span></div>
            <!-- 简介 -->
            <div><span>{{ '用户编号:' + kolInfo.mid }}</span>
              <el-divider direction="vertical"></el-divider>
              <span>{{ '认证:' + kolInfo.title }}</span></div>
            <!-- 签名 -->
            <div><span>{{ '签名:' + kolInfo.sign }}</span></div>
            <!-- tag -->
            <el-tag style="width:45%" type="info">标签</el-tag>
          </div>

          <el-divider></el-divider>
          <div class="mid2" style="display:flex;flex-wrap:wrap;">
            <span>{{ '粉丝量:' + kolInfo.follower }} </span>
            <el-divider direction="vertical"></el-divider>
            <span>{{ '播放量:' + kolInfo.play_view }}</span>
            <el-divider direction="vertical"></el-divider>
            <span>{{ '获赞量:' + kolInfo.likes }}</span>
          </div>
          <el-divider></el-divider>

          <div class="bottom" style="display:flex;flex-wrap:wrap;">
            <!-- 近30天平均数据 -->
            <el-divider direction="vertical"></el-divider>
            <span>{{ '平均播放:' + kolDetail.recent_data.avgs.view_n__avg }}</span>

            <span>{{ '平均点赞:' + kolDetail.recent_data.avgs.like_n__avg }}</span>
            <el-divider direction="vertical"></el-divider>
            <span>{{ '平均投币:' + kolDetail.recent_data.avgs.coin__avg }}</span>

            <span>{{ '平均收藏:' + kolDetail.recent_data.avgs.favorite__avg }}</span>
            <el-divider direction="vertical"></el-divider>
            <span>{{ '平均分享:' + kolDetail.recent_data.avgs.share__avg }}</span>
            <el-divider direction="vertical"></el-divider>
            <span>{{ '平均评论:' + kolDetail.recent_data.avgs.reply__avg }}</span>

          </div>
          <el-divider></el-divider>


        </el-card>
      </el-col>

      <el-col :span="17" style="height:100%">
        <el-card class="right-card" style="height:100%;overflow: auto">
          <el-tabs v-model="activeName">
            <el-tab-pane label="流量分析" name="first">
              <!-- kolStat近几天新增数据表格 -->

              <!-- 粉丝、点赞增量、总量 -->
              <KolLiuLiang :kolDetail="kolDetail"></KolLiuLiang>
              <!-- 近10个视频三连、播放数据 折线图 -->
            </el-tab-pane>
            <el-tab-pane label="作品数据" name="second">作品数据</el-tab-pane>
            <!-- kolinfo作品列表 -->
            <!-- kolinfo多天视频三连、播放数据 折线图 -->

            <el-tab-pane label="舆情分析" name="third">舆情分析</el-tab-pane>
            <!-- 评论热词 弹幕词云 -->
            <el-tab-pane label="粉丝画像" name="fourth">粉丝画像</el-tab-pane>
          </el-tabs>
        </el-card>
      </el-col>

    </el-row>
  </div>

</template>
<script>
import KolLiuLiang from '@/components/Charts/KolLiuLiang.vue'

export default {
  name: 'KolDetail',
  data() {
    return {
      activeName: 'first',
      id: this.$route.query.id,
      kolInfo: ''
    }
  },
  components: {
    KolLiuLiang
  },
  mounted() {
    this.init_info()
    this.init_detail()
  },
  methods: {
    init_info() {
      if (this.$route.query.kolInfo) {
        let kolInfo = decodeURIComponent(this.$route.query.kolInfo)
        this.kolInfo = JSON.parse(kolInfo)
      }
    },
    init_detail() {
      this.getRequest('/kolDetail/' + this.id).then(resp => {
        if (resp) {
          console.log(resp);
          this.$store.commit('INIT_KOLSDETAIL', resp);
        }
      })
    }
  },
  computed: {
    kolDetail() {
      return this.$store.state.kolDetail
    }
  }

}
</script>

<style scoped>


</style>