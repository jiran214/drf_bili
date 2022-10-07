<template>
  <div class="back">
    <el-tabs v-model="activeName" @tab-click="handleClick" style="margin-left:40px;padding-top:20px">
    <el-tab-pane label="个人信息"  name="first">
      <el-form ref="form" label-width="190px" size="small" label-position='top' disabled:0 style="width: 70%;">
      <el-form-item :label="'名称:'+user.name">
      <el-input v-model="userBox.name"></el-input>
      </el-form-item> 
      <el-form-item :label="'性别（male or female）:'+user.gender">
        <el-input v-model="userBox.gender"></el-input>
      </el-form-item> 
      <el-form-item :label="'生日:'+user.birthday" >
      <el-date-picker type="date" placeholder="选择日期" v-model="userBox.birthday" value-format="yyyy-MM-dd" style="width: 100%;"></el-date-picker>
      </el-form-item> 
      <el-form-item :label="'邮箱:'+user.email">
      <el-input v-model="userBox.email"></el-input>
      </el-form-item> 
      <el-form-item :label="'手机:'+user.mobile">
      <el-input v-model="userBox.mobile"></el-input>
      </el-form-item> 
      <el-form-item label='头像:'> 
        <el-upload
        class="avatar-uploader"
        action=""
        :http-request="uploadImg"
        :show-file-list="false"
        name="image"	>
        <el-avatar v-if="user.image" :src="user.image"> user </el-avatar>
        <i v-else class="el-icon-plus avatar-uploader-icon"></i>
      </el-upload>
      </el-form-item> 
      
      
      <el-form-item size="large">
      <el-button type="primary" @click="onSubmit">立即创建</el-button>
      </el-form-item>
    </el-form>
    </el-tab-pane>
    <el-tab-pane label="购买记录" name="second">购买记录</el-tab-pane>
    <el-tab-pane label="账号管理" name="third">账号管理</el-tab-pane>
    <el-tab-pane label="意见反馈" name="fourth">意见反馈</el-tab-pane>
    </el-tabs>
  </div>
  
  
  
</template>
<script>
export default {
    name: 'UserInfo',
    data() {
    return {
      userBox:{
        name:"", gender:"", birthday:"", email:"", mobile:""
      },
      activeName: 'first',
    }
    },
    computed:{
    user() {
      return this.$store.state.user
    }
    },
    mounted(){
      this.init_user()
    },
    methods:{
      handleClick(tab, event) {
        console.log(tab, event);
      },
      onSubmit(){
        // this.userBox.birthday=this.userBox.birthday.substring(10)
        console.log(this.userBox.birthday)
        this.putRequest('/user/1/',this.userBox).then(resp => {
            if (resp) {
                this.$store.commit('INIT_USER', resp);
            }
            })
      },
      init_user(){
        this.getRequest('/user/1/',this.userBox).then(resp => {
            if (resp) {
                this.$store.commit('INIT_USER', resp);
            }
            })
      },
      uploadImg (f) {
            this.progressFlag = true
            let formdata = new FormData()
            formdata.append('image', f.file)
            this.putRequest('/user/1/',formdata).then(resp => {
            if (resp) {
                this.$store.commit('INIT_USER', resp);
            }
            })
        },

    },
    
}
</script>

<style scoped>
.back{
  background-color: white;
  /* height: 100%; */
}
</style>