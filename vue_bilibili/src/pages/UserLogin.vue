<template>
    <div>

        <el-form
            v-loading="loading"
            element-loading-text="正在请求......"
            element-loading-spinner="el-icon-loading"
            element-loading-background="rgba(0, 0, 0, 0.8)"
            ref="loginForm" :model="loginForm" :rules="rules" class="loginContainer">
        <el-radio-group v-model="radioLabel" size="small">
        <el-radio-button label="登录">登录</el-radio-button>
        <el-radio-button label="注册">注册</el-radio-button>
        </el-radio-group>
        <h3 class="loginTitle">{{radioLabel}}</h3>
        <!-- 自动补全 auto-complete="false" -->
        <el-form-item prop="username">
            <el-input type="text" auto-complete="false" v-model="loginForm.username" placeholder="请输入用户名或邮箱"></el-input>
        </el-form-item>
        <el-form-item prop="password">
            <el-input type="password" auto-complete="false" v-model="loginForm.password" placeholder="请输入密码"></el-input>
        </el-form-item>
        <el-form-item prop="code" :class="{'view-active':radioLabel=='登录'}">
            <el-input type="text" auto-complete="false" v-model="code" placeholder="点击图片更换验证码"
                    style="width: 250px;margin-right: 5px;"></el-input>
            <!-- <img :src="captchaUrl" @click="updateCaptcha"> -->
            <el-button type="primary" round @click="send_code">发送验证码</el-button>
        </el-form-item>
        <el-checkbox v-model="checked" class="loginRemember">记住我</el-checkbox>
        <!-- <el-button type="primary" style="float:right" @click="submitReg">登录</el-button> -->
        <el-button type="primary" style="width: 100%" @click="submitLogin">{{radioLabel}}</el-button>
        </el-form>
    </div>
    </template>
    <script>
import { Message } from 'element-ui'
    export default {
    name: 'UserLogin',
    components: {},
    props: [],
    data() {
        return {
        // 验证码
        // captchaUrl: '/captcha?time=' + new Date(),
        code:'',
        radioLabel:'登录',
        loginForm: {
          username: 'admin',
          password: 'admin',
          // code: '',
        },
        regForm: {
        },
        loading: false, // 加载中
        checked: true,
        rules: {
            username: [{required: true, message: '请输入用户名', trigger: 'blur'}],
            password: [{required: true, message: '请输入密码', trigger: 'blur'}],
            // code: [{required: true, message: '请输入验证码', trigger: 'blur'}]
        }
        }
    },
    methods: {
        // 点击刷新验证码
        send_code() {
            this.$refs.loginForm.validate((valid) => {
            if (valid) {
            this.loading = true
            // alert('submit!')
            this.postRequest('/code', {'email':this.regForm.username}).then(resp => {
                // alert(JSON.stringify(resp));
                this.loading = false
                if (resp) {
                    Message.info('发送成功，请填写验证码')
                }

            })
            }
        })
        },
        submitReg() {
            this.$refs.loginForm.validate((valid) => {
            if (valid) {
            this.loading = true
            this.regForm = this.loginForm
            this.regForm['email'] = this.code
            this.postRequest('/user', this.regForm).then(resp => {
                this.loading = false
                if (resp) {
                // 存储用户 token 到 sessionStorage
                const access = resp.data.access
                window.sessionStorage.setItem('access', access)

                // 页面跳转
                // 拿到用户要跳转的路径
                let path = this.$route.query.redirect;
                // 用户可能输入首页地址或错误地址，让他跳到首页，否则跳转到他输入的地址
                this.$router.replace((path === '/' || path === undefined) ? '/UserHome' : path)
                }

            })
            } else {
            this.$message.error('请输入所有字段！')
            return false;
            }

            })
        },

        submitLogin() {
        // 登录
        this.$refs.loginForm.validate((valid) => {
            if (valid) {
            this.loading = true
            // alert('submit!')
            this.postRequest('/login', this.loginForm).then(resp => {
                // alert(JSON.stringify(resp));
                this.loading = false
                if (resp) {
                // 存储用户 token 到 sessionStorage
                const access = resp.data.access
                window.sessionStorage.setItem('access', access)
                // 跳转到首页
                // this.$router.push('/home') // 路由跳转，可以回退到上一页
                // this.$router.replace('/home') // 路径替换，无法回退到上一页

                // 页面跳转
                // 拿到用户要跳转的路径
                let path = this.$route.query.redirect;
                // 用户可能输入首页地址或错误地址，让他跳到首页，否则跳转到他输入的地址
                this.$router.replace((path === '/' || path === undefined) ? '/UserHome' : path)
                }

            })
            } else {
            this.$message.error('请输入所有字段！')
            return false;
            }
        })
        }
    }
    }
    </script>
    <style>
    .view-active {
        display: none;
    }
        
    .loginContainer {
    border-radius: 15px;
    background-clip: padding-box;
    /*属性规定背景的绘制区域 背景被裁剪到内边距框。 margin: 180 px auto;*/
    margin: 180px auto;
    width: 350px;
    padding: 15px 35px;
    background: #fff;
    border: 1px solid #eaeaea;
    box-shadow: 0 0 25px #cac6c6;
    }

    .loginTitle {
    margin: 0 auto 40px auto;
    text-align: center;
    }

    .loginRemember {
    text-align: left;
    margin: 0 0 15px 0;
    }

    /*验证码*/
    .el-form-item__content {
    display: flex;
    align-items: center;
    }
    </style>