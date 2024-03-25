// 创建app
import React, {Component} from "react";
import {BrowserRouter, Route} from 'react-router-dom'; // 引入路由组件
import About from "./pages/About";
import Home from "./pages/Home";
import Idx from "./components/Idx";

// 创建并暴露app
export default class App extends Component {
    render() {
        return (
            // NavLink在激活的时候，会自动加上activeClassName传入的class属性；比link要高级一些；
            <div className="link-bar">
                <BrowserRouter>
                    {/* 路由的索引，导航区，编译之后直接成a标签 */}
                    <Idx to="home">Home</Idx>
                    <Idx to="About" children="About"></Idx>
                <div>
                    {/* 注册路由，使用Route切换页面，作为参数传入route的组件被称作路由组件 */}
                    <Route path="/home" component={Home}></Route>
                    <Route path="/about" component={About}></Route>
                </div>
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