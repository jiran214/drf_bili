const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
    transpileDependencies: true
})

let proxyObj = {} // 代理对象
proxyObj['/'] = {
    // websocket
    ws: false,
    // 代理目标地址
    target: 'http://localhost:8081',
    // 发送请求头 host 会被设置 target
    changeOrigin: true,
    // 不重写请求地址
    pathRewrite: {
        '^/': '/'
    }
}
// 访问的默认的路径和端口
module.exports = {
    devServer: {
        host: 'localhost',
        port: 8080,
        proxy: proxyObj // 代理
    }
}
