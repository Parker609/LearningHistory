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
app.get('/', (req, res) => {
    return res.send('hello express');
});

// 监听3000端口
app.listen(9999); 

*/

// 