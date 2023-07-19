// webpack 的配置包

const path = require('path'); // node的path包引入

// 引入webpackplugin插件
const HTMLWebPlagin = require('html-webpack-plugin');

// webpack的配置文件都写在momdule.exports中；
1
module.exports = {
    // 指定入口文件
    entry: "./src/index.ts",

    // 指定打包后输出文件目录
    output: {
        // 路径
        path: path.resolve(__dirname, 'dist'),
        // 文件名
        filename: "bundle.js",
        // 编译环境设置
        environment: {
            // 是否是用箭头函数，还是别用了，低版本ie不兼容；
            arrowFunction: false 
        }
    },
    // 指定webpack打包的时候使用规则
    module: {
        // 打包规则
        rules: [
            {
                // test指定规则生效文件
                test: /\.ts/, // 正则表达式表示对哪些文件生效
                // 使用ts-loader去处理，use可以有多种格式，可以是简单的string，也可以是[]来处理
                use: [
                    // 使用顺序，由右到左；
                    // babel的处理，可以用 {} 来设置参数
                    {
                        // 使用的loader是啥
                        loader: 'babel-loader',
                        // 参数
                        options: {
                            // 预设的环境
                            presets: [
                                // 指定插件，[插件名+插件设置]、、、、禁止套娃
                                ['@babel/preset-env', {
                                    targets: {
                                        "chrome": "87" // 适配浏览器
                                    },
                                    corejs: 3, // 使用的core的版本，比方说promise的转换，针对一些低版本没有的js的转化；
                                    useBuiltIns: 'usage' // 按需加载
                                }],
                            ], // 使用的预设环境
                        }
                    },
                    // ts的处理
                    'ts-loader'
                ],
                // 要排除的文件，即不处理的文件
                exclude: /node_modules/
            }
        ]
    },
    // 要引入的插件
    plugins: [
        // 自动创建新的plugin，可以有参数，如title，或者可以使用tempalte作为模板；
        new HTMLWebPlagin({
            title: '这是个页面title'
            // 这个地方可以使用template字段，直接拿某个模板
        }),
    ],

    // 可以作为模块使用的文件，不设置会报错
    resolve: {
        // 拓展名
        extensions: ['.ts', '.js']
    }
}