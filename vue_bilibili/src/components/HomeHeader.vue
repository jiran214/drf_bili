<template>
    <div class="header">
        <div class="title">云E办</div>
        <!-- 1-1 添加在线聊天入口 -->
        <div>
            <el-button type="text" icon="el-icon-bell" size="bigger"
                        style="margin-right: 8px;color: black;" @click="goChar"></el-button>
            <el-dropdown class="userInfo" @command="commandHandler">
            <span class="el-dropdown-link">
            <!-- {{ user.name }}<i><img :src="user.userFace"></i> -->
                <el-avatar :src='this.image'> user </el-avatar>
            </span>
            <el-dropdown-menu slot="dropdown">
                <el-dropdown-item command="userinfo">个人中心</el-dropdown-item>
                <el-dropdown-item command="setting">设置</el-dropdown-item>
                <el-dropdown-item command="logout">注销登录</el-dropdown-item>
            </el-dropdown-menu>
            </el-dropdown>
        </div>
    </div>
</template>

<script>

export default {
    name: 'HomeHeader',
    data(){
        return{
            image:""
        }
    },
    
    mounted(){
        this.init_user()
    },
    props: {
        msg: String
    },
    // computed:{
    //     user() {
    //     return this.$store.user
    // }
    // },
    methods:{
        init_user(){
        this.getRequest('/user/1/',this.userBox).then(resp => {
            if (resp) {
                // this.$store.commit('INIT_USER', resp);
                // this.image=this.$store.user.image
                this.image=resp.data.image
            }
            })
    },

    goChar() {
        // this.$router.push('/home')
    },
    // 注销登录
    commandHandler(command) {
        console.log(command)
        if (command === 'logout') {
        // 弹框提示用户是否要删除
        this.$confirm('此操作将注销登录, 是否继续?', '提示', {
            confirmButtonText: '确定',
            cancelButtonText: '取消',
            type: 'warning'
        }).then(() => {

            // 清空用户信息
            window.sessionStorage.removeItem('access')
            window.sessionStorage.removeItem('user')
            // 路由替换到登录页面
            // this.$router.replace('/')
            // 清空菜单信息；在src/utils/menus.js 中初始化菜单信息
            this.$router.replace('/')
        }).catch(() => {
            this.$message({
            type: 'info',
            message: '已取消注销登录'
            });
        });
        }
        if (command === 'userinfo') {
        this.$router.push('/UserInfo')
        }
    }
    }
}
</script>

<style scoped>
.title {
    font-size: 30px;
    /*font-family: 微软雅黑;*/
    font-family: 华文楷体;
    color: white;
}

.header{
    background-color: white;
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-sizing: border-box;

}

.userInfo {
    cursor: pointer;
}

.el-dropdown-link img {
    width: 48px;
    height: 48px;
    border-radius: 50%;
    margin-left: 8px;
    }
.el-avatar{
    margin-left: 10px;
    margin-right: 10px;
    margin-top: 10px;
}
</style>