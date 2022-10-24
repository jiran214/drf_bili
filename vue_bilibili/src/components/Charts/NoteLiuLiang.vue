<template>
  <div>
    <el-radio-group v-model="sanlianType" style="">
      <el-radio-button label="总量"></el-radio-button>
      <el-radio-button label="增量"></el-radio-button>
    </el-radio-group>
    <div id="sanlian" style="width: 900px; height: 400px;margin-top:20px"></div>
    <!-- <span>{{sanlianData}}</span> -->
    <el-radio-group v-model="hudongType" style="">
      <el-radio-button label="总量"></el-radio-button>
      <el-radio-button label="增量"></el-radio-button>
    </el-radio-group>
    <div id="hudong" style="width: 900px; height: 400px;margin-top:20px"></div>
  </div>
</template>

<script>
export default {
  props: [
    'noteDetail'
  ],
  name: 'NoteLiuLiang',
  data() {
    return {
      sanlianType: '总量',
      hudongType: '总量',

    }
  },
  computed: {
    sanlianData() {
      if (this.sanlianType == '总量') {
        return this.noteDetail.states.all
      } else {
        return this.noteDetail.states.ins
      }
    },
    hudongData() {
      if (this.hudongType == '总量') {
        return this.noteDetail.states.all
      } else {
        return this.noteDetail.states.ins
      }
    }
  },
  mounted() {
    this.Sanlian()
    this.Hudong()
  },
  watch: {
    // 被监视的属性
    sanlianType: {
      // 属性变化的回调函数
      handler(newValue, oldValue) {
        console.log('属性被修改了', newValue, oldValue);
        this.Sanlian()
      }
    },
    hudongType: {
      // 属性变化的回调函数
      handler() {
        this.Hudong()
      }
    }
  },
  methods: {
    Sanlian() {
      let SanlianChart = this.$echarts.init(document.getElementById("sanlian"));
      let option = {
        title: {
          text: '三连趋势变化'
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'cross',
            label: {
              backgroundColor: '#6a7985'
            }
          }
        },
        legend: {
          data: ['点赞', '投币', '收藏']
        },
        toolbox: {
          feature: {
            saveAsImage: {}
          }
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
        },
        xAxis: [
          {
            type: 'category',
            boundaryGap: false,
            data: this.sanlianData.ctime
          }
        ],
        yAxis: [
          {
            type: 'value'
          }
        ],
        series: [
          {
            name: '点赞',
            type: 'line',
            stack: 'Total',
            areaStyle: {},
            emphasis: {
              focus: 'series'
            },
            data: this.sanlianData.like_n_y
          },
          {
            name: '投币',
            type: 'line',
            stack: 'Total',
            areaStyle: {},
            emphasis: {
              focus: 'series'
            },
            data: this.sanlianData.coin_y
          },
          {
            name: '收藏',
            type: 'line',
            stack: 'Total',
            label: {
              show: true,
              position: 'top'
            },
            areaStyle: {},
            emphasis: {
              focus: 'series'
            },
            data: this.sanlianData.favorite_y
          }
        ]
      };
      SanlianChart.setOption(option);

    },
    Hudong() {
      let HudongChart = this.$echarts.init(document.getElementById("hudong"));
      let option = {
        title: {
          text: '互动趋势变化'
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'cross',
            label: {
              backgroundColor: '#6a7985'
            }
          }
        },
        legend: {
          data: ['播放', '弹幕', '评论', '分享']
        },
        toolbox: {
          feature: {
            saveAsImage: {}
          }
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
        },
        xAxis: [
          {
            type: 'category',
            boundaryGap: false,
            data: this.hudongData.ctime
          }
        ],
        yAxis: [
          {
            type: 'value'
          }
        ],
        series: [
          {
            name: '播放',
            type: 'line',
            stack: 'Total',
            areaStyle: {},
            emphasis: {
              focus: 'series'
            },
            data: this.hudongData.view_n_y
          },
          {
            name: '弹幕',
            type: 'line',
            stack: 'Total',
            areaStyle: {},
            emphasis: {
              focus: 'series'
            },
            data: this.hudongData.danmaku_y
          },
          {
            name: '评论',
            type: 'line',
            stack: 'Total',
            label: {
              show: true,
              position: 'top'
            },
            areaStyle: {},
            emphasis: {
              focus: 'series'
            },
            data: this.hudongData.reply_y
          },
          {
            name: '分享',
            type: 'line',
            stack: 'Total',
            label: {
              show: true,
              position: 'top'
            },
            areaStyle: {},
            emphasis: {
              focus: 'series'
            },
            data: this.hudongData.share_y
          }
        ]
      };
      HudongChart.setOption(option);
    }
  }
}
</script>

<style>

</style>