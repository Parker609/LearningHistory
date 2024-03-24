// 给react用的，其实是通过这个文件配置http-proxy-middleware的node中间件；

// 获取中间件
const {createProxyMiddleware} = require('http-proxy-middleware');

// 通过中间件将请求代理到了8000接口；
module.exports = function(app) {
    app.use(
        createProxyMiddleware('/api', {
            target: 'http://localhost:8000',
            changeOrigin: true, // 真正请求的时候，不使用请求的域名，而是用代理之后的域名；
            pathRewrite: {'/api': ''} // api是代理的标示，不能真的用它来请求；
        })
    )
}