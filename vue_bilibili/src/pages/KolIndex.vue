<template>
    <el-main>
        <el-card class="box-card" >
        <div slot="header" class="clearfix">
            <span>up主搜索：根据名称、mid、tag、签名</span>
            <div style="margin-top: 15px;">
            <el-input placeholder="请输入内容" v-model="requestParams.search" class="input-with-select">
                <el-select v-model="select" slot="prepend" placeholder="请选择">
                <el-option label="Uid" value="1"></el-option>
                <el-option label="订单号" value="2"></el-option>
                <el-option label="用户电话" value="3"></el-option>
                </el-select>
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
            <span class="view-title">up主信息:</span>
            
            <span class="tab">认证</span>
            <el-select v-model="requestParams.role_type" placeholder="不限">
            <el-option
                v-for="item in upOptions.rz"
                :key="item.value"
                :label="item.label"
                :value="item.value">
            </el-option>
            </el-select>
            
            <span class="tab">性别</span>
            <el-select v-model="requestParams.sex" placeholder="全部">
            <el-option
                v-for="item in upOptions.sex"
                :key="item.value"
                :label="item.label"
                :value="item.value">
            </el-option>
            </el-select>
            
            <span class="tab">等级</span>
            <el-select v-model="requestParams.user_level" placeholder="不限">
            <el-option
                v-for="item in upOptions.level"
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
            <span :class="{'view-active': order.follower}" @click="orderClick('follower')">粉丝数排序</span>
            <span :class="{'view-active': order.play_view}" @click="orderClick('play_view')">播放量排序</span>
            <span :class="{'view-active': order.likes}" @click="orderClick('likes')">点赞量排序</span>
            </div>
            </div>
        </div>
        
        <!-- 循环卡片 -->
        <div class="list">
            <el-card class="box-cards" v-for="(kol,index) in this.$store.state.kols" :key="index">
            <div slot="header" class="clearfix" style="display: flex;">
                <div class="left" style="">
                    <!-- 头像 -->
                    <div><el-avatar src='https://imgs-bz.feigua.cn/bfs/face/84e626cf46d0b4f0e79d4158387b1719df306a92.jpg' :size=120></el-avatar></div>
                </div>
                <div class="mid" style="margin-left:20px  ;flex:1;display:flex;flex-direction: column;justify-content: space-around;">
                    <!-- 名称 -->
                    <div><span style="font-weight:1000">{{kol.user_name}}</span>
                        <el-divider direction="vertical"></el-divider>
                        <span>{{'用户等级:'+kol.user_level}}</span></div>
                    <!-- 简介 -->
                    <div><span>{{'用户编号:'+kol.mid}}</span>
                        <el-divider direction="vertical"></el-divider>
                        <span>{{'认证:'+kol.title}}</span></div>
                    <!-- 签名 -->
                    <div><span>{{'签名:'+kol.sign}}</span></div>
                    <!-- tag -->
                    <el-tag type="info">标签三</el-tag>
                </div>
                <div class="right" style="display: flex;flex-direction: column;align-items: center;">
                    <el-button style="width: 100px;margin-top: 20px;" type="danger" plain>添加收藏</el-button>
                    <el-button style="width: 100px;margin-right: 10px;margin-top: 15px;" type="danger" plain>查看详情</el-button>
                </div>
                
                
            </div>
            <div class="text item" style="display:flex;justify-content: space-around;">
                <span>{{'粉丝量:'+kol.follower}} </span>
                <el-divider direction="vertical"></el-divider>
                <span>{{'播放量:'+kol.play_view}}</span>
                <el-divider direction="vertical"></el-divider>
                <span>{{'获赞量:'+kol.likes}}</span>
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
    name: 'KolIndex',
    data() {
    return {
        // 分页
        curPage: 1, // 当前页数
        list: [], // 角色列表
        total: 0, // 一共几条数据
        // 搜索
        input:'',
        select:'',
        isShow: false,
        order:{follower:true,play_view:false,likes:false},
        requestParams : {
            page: '1',
            page_size: '10',

            sex: '',
            user_level: '',
            notes__id: '',
            role_type: '',

            followermin: '',
            followermax: '',
            title: '',
            notes_title: '',
            search: '',
            ordering: '-follower',
        },
        filterBox: [
        {
            name: "类别:",
            items: [
            { value: "1", text: "全部", active: true },
            { value: "2", text: "动物圈", active: false },
            { value: "3", text: "国创", active: false },
            { value: "2", text: "运动", active: false },
            { value: "3", text: "汽车", active: false },
            { value: "2", text: "美食", active: false },
            { value: "3", text: "番剧", active: false },
            { value: "2", text: "动画", active: false },
            { value: "3", text: "科技", active: false },
            { value: "2", text: "游戏", active: false },
            { value: "3", text: "知识", active: false },
            { value: "2", text: "生活", active: false },
            { value: "3", text: "时尚", active: false },
            { value: "2", text: "鬼畜", active: false },
            { value: "2", text: "音乐", active: false },
            { value: "3", text: "舞蹈", active: false },
            { value: "2", text: "娱乐", active: false },
            ],
        },
        {
            name: "粉丝:",
            items: [
            { value: "", text: "全部", active: true },
            { value: ";10000", text: "1万以下", active: false },
            { value: ";100000", text: "1-10万", active: false },
            { value: "100000;200000", text: "10-20万", active: false },
            { value: "200000;300000", text: "20-30万", active: false },
            { value: "300000;500000", text: "30-50万", active: false },
            { value: "500000;1000000", text: "50-100万", active: false },
            { value: "2000000;3000000", text: "200-300万", active: false },
            { value: "3000000;5000000", text: "300-500万", active: false },
            { value: "5000000;10000000", text: "500-1000万", active: false },
            { value: "10000000;;", text: "1000万以上", active: false },
            ],
        },
        {
            name: "报价:",
            items: [
            { value: "allSex", text: "全部", active: true },
            { value: "allAge", text: "5000以下", active: false },
            { value: "treeY", text: "5000-1万", active: false },
            { value: "fourteenY", text: "1万-5万", active: false },
            { value: "fortyY", text: "5万-10万", active: false },
            ],
        },
        ],
        upOptions: {rz:[{value: '',label: '全部'}, {value: '0',label: '无'}, {value: '1',label: '个人认证'}, {value: '2',label: '机构认证'}],
                    sex:[{value: '',label: '全部'}, {value: '男',label: '男'},{value: '女',label: '女'},{value: '选项3',label: '保密'}],
                    level:[{value: '',label: '全部'}, {value: '0',label: 'Lv0'},{value: '1',label: 'Lv1'},{value: '2',label: 'Lv2'},{value: '3',label: 'Lv3'},
                    {value: '4',label: 'Lv4'},{value: '5',label: 'Lv5'},{value: '6',label: 'Lv6'}]
        },

    }
    },
    methods:{
        // 分页
        hCurrentChange(curPage) {
            // alert(curPage)
            // 1. 更新页码
            this.pageParams.page = curPage
            // 2. 重发请求
        },

        orderClick(k){
            // 添加 active ==> true 显示 `active样式`
            this.order.follower=false
            this.order.play_view=false
            this.order.likes=false
            this.order[k] = true
            this.requestParams.ordering='-'+k
        },
        tabClick(v,t,k){
            this.filterBox[k].items.map(item => {
                item.active = false
            })
            this.filterBox[k].items[t].active = true

            if(k=='1'){
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
            this.getRequest('/kol',newV).then(resp => {
            if (resp) {
                console.log(resp);
                this.$store.commit('INIT_KOLS', resp);
                this.total=resp.data.count
            }
            })
        },
        deep:true, //true 深度监听
        immediate: true,
    },
    computed: {
        // kols(){return }
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