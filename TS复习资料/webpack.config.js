// webpack 的配置包

const path = require('path'); // node的path包引入

// webpack的配置文件都写在momdule.exports中；

module.exports = {
    // 指定入口文件
    entry: "./src/index.ts",

    // 指定打包后输出文件目录
    output: {
        // 路径
        path: path.resolve(__dirname, 'dist'),
        // 文件名
        filename: "bundle.js"
    },
    // 指定webpack打包的时候使用规则
    module: {
        // 打包规则
        rules: [
            {
                // test指定规则生效文件
                test: /\.ts/, // 正则表达式表示对哪些文件生效，这个正则不知道是否是js的正则
                // 使用ts-loader去处理
                use: 'te-loader',
                // 要排除的文件，即不处理的文件
                exclude: /node_modules/
            }
        ]
    }
}