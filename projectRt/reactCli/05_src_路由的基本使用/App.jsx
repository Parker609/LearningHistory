// 创建app
import React, {Component} from "react";
import {Link, BrowserRouter, Route} from 'react-router-dom'; // 引入路由组件
import About from "./components/About";
import Home from "./components/Home";
import Idx from "./components/Idx";

// 创建并暴露app
export default class App extends Component {
    render() {
        return (
            <div className="link-bar">
                <BrowserRouter>
                    {/* 路由的索引，导航区，编译之后直接成a标签 */}
                    <Link to="home">Home</Link>
                    <Link to="about">About</Link>
                <div>
                    {/* 注册路由，使用Route切换页面 */}
                    <Route path="/home" component={Home}></Route>
                    <Route path="/about" component={About}></Route>
                </div>
                </BrowserRouter>
            </div>
        )
    }
}