<template>
  <div>
    <!-- <span>{{hudongData}}</span> -->
    <el-radio-group v-model="hudongType" style="">
      <el-radio-button label="总量"></el-radio-button>
      <el-radio-button label="增量"></el-radio-button>
    </el-radio-group>
    <div id="hudong" style="width: 900px; height: 400px;margin-top:20px"></div>
    <div id="tennotes" style="width: 900px; height: 550px;margin-top:20px"></div>
  </div>
</template>

<script>
export default {
  props: [
    'kolDetail'
  ],
  name: 'KolLiuLiang',
  data() {
    return {
      hudongType: '总量',

    }
  },
  computed: {

    hudongData() {
      if (this.hudongType == '总量') {
        return this.kolDetail.states.all
      } else {
        return this.kolDetail.states.ins
      }
    },
    tenNotesData() {
      return this.kolDetail.recent_data.ten_notes
    }
  },
  mounted() {
    this.Hudong()
    this.tenNotes()
  },
  watch: {
    // 被监视的属性
    hudongData: {
      // 属性变化的回调函数
      handler(newValue, oldValue) {
        console.log('属性被修改了', newValue, oldValue);
        this.Hudong()
      }
    },
    tenNotesData: {
      // 属性变化的回调函数
      handler() {
        this.tenNotes()
      }
    }
  },
  methods: {
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
          data: ['播放', '点赞', '关注']
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
            data: this.hudongData.play_view_y
          },
          {
            name: '点赞',
            type: 'line',
            stack: 'Total',
            areaStyle: {},
            emphasis: {
              focus: 'series'
            },
            data: this.hudongData.likes_y
          },
          {
            name: '关注',
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
            data: this.hudongData.follower_y
          }
        ]
      };
      HudongChart.setOption(option);
    },
    tenNotes() {
      let NotesChart = this.$echarts.init(document.getElementById("tennotes"));
      let option = {
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'cross',
            crossStyle: {
              color: '#999'
            }
          }
        },
        toolbox: {
          feature: {
            dataView: {show: true, readOnly: false},
            magicType: {show: true, type: ['line', 'bar']},
            restore: {show: true},
            saveAsImage: {show: true}
          }
        },
        legend: {
          data: ['点赞', '投币', '收藏', '播放']
        },
        xAxis: [
          {
            type: 'category',
            data: this.tenNotesData.ten_pubdate,
            axisPointer: {
              type: 'shadow'
            }
          }
        ],
        yAxis: [
          {
            type: 'value',
            name: '播放数',
          },
          {
            type: 'value',
            name: '三连数',
          }
        ],
        series: [
          {
            name: '点赞',
            type: 'line',
            data: this.tenNotesData.ten_like_n
          },
          {
            name: '投币',
            type: 'line',
            data: this.tenNotesData.ten_coin
          },
          {
            name: '收藏',
            type: 'line',
            data: this.tenNotesData.ten_favorite
          },
          {
            name: '播放',
            type: 'bar',
            data: this.tenNotesData.ten_view_n
          }
        ]
      };
      NotesChart.setOption(option);
    },
  }
}
</script>

<style>

</style>