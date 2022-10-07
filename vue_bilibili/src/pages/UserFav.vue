<template>
    <div class="back">
    <el-tabs v-model="activeName" @tab-click="handleClick" style="margin-left:40px;padding-top:20px">
    <el-tab-pane label="收藏的up主"  name="first">
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
    </el-tab-pane>
    <el-tab-pane label="收藏的素材" name="second">购买记录</el-tab-pane>
    <el-tab-pane label="收藏的商品" name="third">账号管理</el-tab-pane>
    <el-tab-pane label="收藏的品牌" name="fourth">意见反馈</el-tab-pane>
    </el-tabs>
    </div>
    
</template>
<script>
export default {
    name: 'UserFav',
    data() {
    return {
        activeName:'first'
    }
    },
    methods:{
        handleClick(tab, event) {
        console.log(tab, event);
    },
    }
}
</script>

<style>

.back{
    background-color: white;
    /* height: 100%; */
}
</style>