// 创建app
import React, {Component} from "react";
import {BrowserRouter, Route, Redirect} from 'react-router-dom'; // 引入路由组件
import About from "./pages/About";
import Home from "./pages/Home";
import Idx from "./components/Idx";

// 创建并暴露app
// 目前怀疑路由的是需要基于服务器，如果服务器不支持模糊匹配，那么页面的第一次出现就会有问题；
export default class App extends Component {
    render() {
        const a = 'a';
        const b = 'b';
        return (
            // NavLink在激活的时候，会自动加上activeClassName传入的class属性；比link要高级一些；
            <div className="link-bar">
                <BrowserRouter>
                    {/* 通过params来传递参数 */}
                    <Idx to={`/home?a=a&b=b`}>Home</Idx>
                    {/* 模糊匹配，是可以匹配上的，默认模糊匹配 */}
                    <Idx to="/about" children="About"></Idx>
                <div>
                    {/* 当存在多个路由能匹配时，是会都展示的 */}
                    {/* 通过:a的样式来接收params参数 */}
                    <Route path="/home" component={Home}></Route>
                    <Route path="/about" component={About}></Route>
                    {/* 路由都没有匹配上，则redirect指向默认指向的地址 */}
                    <Redirect to="/home"/>
                </div>
                <hr />
                </BrowserRouter>
            </div>
        )
    }
}
/**
 * 路由组件和一般组件的不同：
 * 1. 写法不同：
 *      路由组件写在route中，通过component传入的；
 *      一般组件直接写，直接渲染；
 * 2. 接收到的props不同：
 *      路由组件收到三个大属性；
 *      一般组件收到什么展示什么；
 * 3. 文件存放位置不同：
 *      路由组件一般写在pages里；
 *      一般组件写在component里；
 * 
 */