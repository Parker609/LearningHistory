/**

// express基本使用；
// 在使用过程中的感受就是对node的原生请求方法（http）等做了更高级的封装；
// 1. 引入express模块
// 2. 创建app对象
// 3. 绑定事件
// 4. 启动服务，监听端口

const express = require('express'); // 获取express模块
const app = express(); // 创建app对象
// 绑定事件，监听最外层路径
// 通过res提供的send方法，将值返回并展示
app.get('/', (req, res) => {
    return res.send('hello express');
});

// 监听3000端口
app.listen(9999); 

*/

// express中间件
// express中间件其实就是一堆方法，通过app.use()来注册中间件，是请求处理函数；
// post请求：
const express = require('express');
const app = express();
// app.get('请求路径', '处理函数');
// app.post('请求路径', '处理函数')
// 可以直接写在请求里，但是一般不这么用，一般是写在use里
// use表示所有请求都要经过处理方式；
// app.use('请求地址（可以省略）', '中间件方法')，例：
const toUpper = function(req, res, next) {
    /**
     * 入参有三个：
     *  1. req：http请求的常用参数，常用的参数包括
     *      params：post请求的参数信息
     *      query：get请求的参数信息
     *      body：请求体，一般是undefined，需要特殊的插件才能解析
     *      headers：请求头，cookie，na之类的信息都是在这边携带的
     *      method：请求方法
     *      还有一些其他属性，如：baseUrl，app，fresh，hostname之类的
     *      详细可以参考：https://express.nodejs.cn/
     * 
     *  2. res：http的response参数，常用的方法和参数包括：
     */
    console.log(req.baseUrl);
};
app.use(toUpper);
app.listen(9999)


