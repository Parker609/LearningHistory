// 在react项目中加入请求，这里为了说明请求代理，添加express组件来说明；

const express = require('express');
const app = express();

app.get('/test', (req, res) => {
    console.log('获取到了请求');
    res.send([
        {id: 0, name: 'lisi', age: 18}
    ]);
})

app.listen(8000);