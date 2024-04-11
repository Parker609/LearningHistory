// 创建app
import React, {Component} from "react";
import {BrowserRouter, Route, Redirect, withRouter} from 'react-router-dom'; // 引入路由组件
import About from "./pages/About";
import Home from "./pages/Home";
import Idx from "./components/Idx";
import Header from "./components/Header";

// 创建并暴露app
// 目前怀疑路由的是需要基于服务器，如果服务器不支持模糊匹配，那么页面的第一次出现就会有问题；
export default class App extends Component {
    render() {
        console.log(this.props)
        return (
            // NavLink在激活的时候，会自动加上activeClassName传入的class属性；比link要高级一些；
            <div className="link-bar">
                <BrowserRouter>
                    <Header></Header>
                    {/* 路由的索引，导航区，编译之后直接成a标签 */}
                    {/* 通过state传递参数，to传递的将不是字符串，而是对象 */}
                    <Idx to={{pathname: '/home', state: {a: '11', b: 'test'}}}>Home</Idx>
                    {/* 模糊匹配，是可以匹配上的，默认模糊匹配 */}
                    {/* replace标识replace压栈 */}
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
 * browserRouter和hashRouter，常用browserRouter，毕竟调用了浏览器的history，会协助存储一些数据，不会在页面刷新的时候丢失；
 */