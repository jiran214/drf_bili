<template>
    <el-main>
        <el-card class="box-card" >
        <div slot="header" class="clearfix">
          <i class="el-icon-search"></i><span style="weight:900px">视频搜索:  根据简介、标题</span>
          <div style="margin-top: 15px;">
            <el-input placeholder="请输入内容" v-model="requestParams.search" class="input-with-select">
              <el-button slot="append" icon="el-icon-search" color="rgb(218, 50, 55)"></el-button>

            </el-input>
          </div>
        </div>
        <div class="view-flex" v-for="(item,k) in filterBox" :key="k+'a'">
            <span class="view-title">{{item.name}}</span>
            <div class="view-content" >
                <div class="view-tab" :class="isShow ? 'view-hide' : ''">
                    <span v-for="(v,t) in item.items" :key="t+'b'" :class="{'view-active': v.active}" @click="tabClick(v,t,k)">
                        {{v.text}}</span>
                </div>
            </div>
        </div>
        <el-divider></el-divider>
        <div class="text item">
            <span class="view-title">视频基本信息:</span>
            
            <span class="tab">视频类型</span>
            <el-select v-model="requestParams.copyright" placeholder="不限">
            <el-option
                v-for="item in VideoOptions.copyright"
                :key="item.value"
                :label="item.label"
                :value="item.value">
            </el-option>
            </el-select>
            
            <span class="tab">团队类型</span>
            <el-select v-model="wait" placeholder="全部">
            <el-option
                v-for="item in VideoOptions.sex"
                :key="item.value"
                :label="item.label"
                :value="item.value">
            </el-option>
            </el-select>
            
            <span class="tab">活动类型</span>
            <el-select v-model="wait" placeholder="全部">
            <el-option
                v-for="item in VideoOptions.level"
                :key="item.value+'c'"
                :label="item.label"
                :value="item.value">
            </el-option>
            </el-select>
        </div>
        </el-card>
        
        <!-- 排序 -->
        <div class="view-flex" style="margin-top:20px">
            <span class="view-title" style="margin-right:20px ;">排序方式</span>
            <div class="view-content" >
            <div class="view-tab" :class="isShow ? 'view-hide' : ''">
            <span :class="{'view-active': order[0].active}" @click="orderClick(0)">综合排序</span>
            <span :class="{'view-active': order[1].active}" @click="orderClick(1)">播放排序</span>
            <span :class="{'view-active': order[2].active}" @click="orderClick(2)">收藏排序</span>
            <span :class="{'view-active': order[3].active}" @click="orderClick(3)">投币排序</span>
            <span :class="{'view-active': order[4].active}" @click="orderClick(4)">分享排序</span>
            <span :class="{'view-active': order[5].active}" @click="orderClick(5)">喜欢排序</span>
            </div>
            </div>

            <span>共搜索到<span style="color:red">{{ total }}</span>个结果</span>
        </div>

        
        
        <!-- 循环卡片 -->
        <div class="list">
            <el-card class="box-cards" v-for="(note,index) in this.$store.state.notes" :key="index">
            <div slot="header" class="clearfix" style="display: flex;">
                <div class="left" style="">
                    <!-- 封面 -->
                    <div><a :href=note.short_link><el-avatar :src=note.pic :size=120></el-avatar></a></div>
                </div>
                <div class="mid" style="margin-left:20px  ;flex:1;display:flex;flex-direction: column;justify-content: space-around;">
                    <!-- 标题 -->
                    <div><a :href=note.short_link style="text-decoration: none; color: #444;">
                    <span  style="font-weight:1000">{{note.title}}</span>
                    </a></div>
                  <!-- 简介 -->
                  <div><span>{{ '简介:' + note.desc }}</span>
                    <!-- 作者 时间 分区 -->
                    <div><span style="font-weight:800">{{ '作者:' + note.name }}</span>
                      <el-divider direction="vertical"></el-divider>
                      <span>{{ '时间:' + note.ctime }}</span>
                      <el-divider direction="vertical"></el-divider>
                      <span>{{ '分区:' + note.tname }}</span></div>
                  </div>
                  <!-- tag -->
                  <div style="display:flex;">
                    <el-tag v-for="(tag,index) in note.tags" :key="index" style="margin-right: 10px" type="info">
                      <span>{{ tag }}</span></el-tag>
                  </div>

                </div>
              <div class="right" style="display: flex;flex-direction: column;align-items: center;">
                <el-button style="width: 100px;margin-top: 20px;" type="danger" plain>添加收藏</el-button>
                <el-button plain style="width: 100px;margin-right: 10px;margin-top: 15px;" type="danger"
                           @click="goDetail(note.id,note)">
                  视频分析
                </el-button>
              </div>
                
                
            </div>
            <div class="text item" style="display:flex;justify-content: space-around;">

                <span>{{'播放:'+note.view_n}} </span>
                <el-divider direction="vertical"></el-divider>
                <span>{{'点赞:'+note.like_n}}</span>
                <el-divider direction="vertical"></el-divider>
                <span>{{'投币:'+note.coin}}</span>
                <el-divider direction="vertical"></el-divider>
                <span>{{'收藏:'+note.favorite}} </span>
                <el-divider direction="vertical"></el-divider>
                <span>{{'弹幕:'+note.danmaku}}</span>
                <el-divider direction="vertical"></el-divider>
                <span>{{'评论:'+note.reply}}</span>
                <el-divider direction="vertical"></el-divider>
                <span>{{'分享:'+note.share}}</span>

            </div>
            </el-card>
        </div>
        
        <!-- 分页组件 -->
        <!-- total, sizes, prev, pager, next, jumper -->
        <div style="text-align: center;">
            <el-pagination 
            layout="total,prev,pager,next,jumper"
            :total="total"
            :current-page.sync="requestParams.page"
            @current-change="hCurrentChange"
        />
        </div>
        
    </el-main>
    
    
</template>
<script>
export default {
    name: 'NoteIndex',
    data() {
    return {
        wait:'',
        // 分页
        curPage: 1, // 当前页数
        list: [], // 角色列表
        total: 0, // 一共几条数据
        // 搜索
        input:'',
        select:'',
        isShow: false,
        
        order:[
            {value:'zonghe',active:false},
            {value:'view_n',active:true},
            {value:'favorite',active:false},
            {value:'coin',active:false},
            {value:'share',active:false},
            {value:'like_n',active:false},
        ],
        requestParams : {
            page: '1',
            page_size: '10',
            tid: '',
            category: '',
            copyright: '',
            view_n_max: '',
            view_n_min: '',
            danmaku_max: '',
            danmaku_min: '',
            reply_max: '',
            reply_min: '',
            favorite_max: '',
            favorite_min: '',
          coin_max: '',
          coin_min: '',
          share_max: '',
          share_min: '',
          like_n_max: '',
          like_n_min: '',
          duration_min: '',
          duration_max: '',
          pubdate: '',
          search: '',
          ordering: '-view_n',
          tag: ''
        },
        filterBox: [
        {
            name: "分区:",
            items: [
            { value: "", text: "全部", active: true },
            { value: "动物圈", text: "动物圈", active: false },
            { value: "国创", text: "国创", active: false },
            { value: "运动", text: "运动", active: false },
            { value: "汽车", text: "汽车", active: false },
            { value: "美食", text: "美食", active: false },
            { value: "番剧", text: "番剧", active: false },
            { value: "动画", text: "动画", active: false },
            { value: "科技", text: "科技", active: false },
            { value: "游戏", text: "游戏", active: false },
            { value: "知识", text: "知识", active: false },
            { value: "生活", text: "生活", active: false },
            { value: "时尚", text: "时尚", active: false },
            { value: "鬼畜", text: "鬼畜", active: false },
            { value: "音乐", text: "音乐", active: false },
            { value: "舞蹈", text: "舞蹈", active: false },
            { value: "娱乐", text: "娱乐", active: false },
            ],
        },
        {
            name: "热门标签:",
            items: [
            { value: "", text: "全部", active: true },
            { value: "电脑", text: "电脑", active: false },
            { value: "买房", text: "买房", active: false },
            { value: "眼妆", text: "眼妆", active: false },
            { value: "上色", text: "上色", active: false },
            { value: "啤酒", text: "啤酒鸭", active: false },
            { value: "手办", text: "手办", active: false },
            { value: "模型", text: "模型", active: false },
            { value: "萌娃", text: "萌娃", active: false },
            { value: "料理", text: "料理", active: false },
            { value: "舞蹈", text: "舞蹈", active: false },
            ],
        },
        {
            name: "发布时间:",
            items: [
            { value: "", text: "全部", active: true },
            { value: "1", text: "近24小时", active: false },
            { value: "1", text: "近1天", active: false },
            { value: "7", text: "近7天", active: false },
            { value: "30", text: "近30天", active: false },
            ],
        },
        ],

        VideoOptions: {copyright:[{value: '',label: '全部'}, {value: '1',label: '原创'}, {value: '2',label: '转载'}],
                    sex:[{value: '',label: '全部'}, {value: '男',label: '男'},{value: '女',label: '女'},{value: '选项3',label: '保密'}],
                    level:[{value: '',label: '全部'}, {value: '0',label: 'Lv0'},{value: '1',label: 'Lv1'},{value: '2',label: 'Lv2'},{value: '3',label: 'Lv3'},
                    {value: '4',label: 'Lv4'},{value: '5',label: 'Lv5'},{value: '6',label: 'Lv6'}]
        },

    }
    },
    methods: {
      // 详情页
      goDetail(id, note) {
        let routeUrl = this.$router.resolve({
          path: '/NoteDetail',
          query: {
            id: id,
            noteInfo: encodeURIComponent(JSON.stringify(note)),
          }
        })
        window.open(routeUrl.href, '_blank')
      },

      // 分页
      hCurrentChange(curPage) {
        // alert(curPage)
        // 1. 更新页码
        this.pageParams.page = curPage
        // 2. 重发请求
      },

      orderClick(k) {
            // 添加 active ==> true 显示 `active样式`
            this.order.map(item => {
                item.active = false
            })
            this.order[k].active = true
            this.requestParams.ordering='-'+this.order[k].value
        },
        tabClick(v,t,k){
            this.filterBox[k].items.map(item => {
                item.active = false
            })
            this.filterBox[k].items[t].active = true

            if(k=='0'){
                this.requestParams.category=v.value
            }

            if(k=='1'){
                this.requestParams.tag=v.value
            }
            
            if(k=='2'){
                this.requestParams.pubdate=v.value
            }

            if(k=='3'){
                let array=v.value.split(';')
                let followerMin=array[0]
                let followerMax=array[1]
                this.requestParams.followermin=followerMin
                this.requestParams.followermax=followerMax
            }
        }
    },
    watch:{
        requestParams:{//深度监听，可监听到对象、数组的变化
        handler:function(newV){
            this.getRequest('/note',newV).then(resp => {
            if (resp) {
                console.log(resp);
                this.$store.commit('INIT_NOTES', resp);
                this.total=resp.data.count
            }
            })
        },
        deep:true, //true 深度监听
        immediate: true,
    },
    computed: {
        // notes(){return }
    }

}
}
</script>

<style>

.el-button--danger.is-disabled:hover{
    background-color: rgb(9, 8, 8);
    border: 1px solid #ccc;
    
}

.box-cards{
    margin-bottom: 25px;
}

.el-select .el-input {
    width: 130px;
    }
    .input-with-select .el-input-group__prepend {
    background-color: #fff;
    }

.category{
    display:flex;
    margin-right: 10;
}

/* 多条筛选样式 */
.tab{
    margin-left:75px ;
    margin-right:20px ;
}
.view-flex {
	display: flex;
	margin-bottom: 15px;
}

.view-title {
	flex-basis: 70px;
	margin-top: 5px;
}

.view-content {
	display: flex;
	flex: 1;
}

.view-tab {
	flex: 1;
	margin-right: 15px;
	height: 35px;
	overflow: hidden;
}

.view-tab span {
	display: inline-block;
	margin: 0 5px 15px 5px;
	cursor: pointer;
	padding: 5px 10px;
	color: #999999;
}

.view-active {
	background-color:rgb(218, 50, 55);
	color: white !important;
	border-radius: 3px;
}

.view-tab span:hover {
	background-color:rgb(218, 50, 55);
	color: white;
	border-radius: 3px;
}

.view-hide {
	min-height: 35px;
	height: auto !important;
}

</style>