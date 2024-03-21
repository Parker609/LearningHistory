// 创建app
import React, {Component} from "react";
// import应用的组件
import Hello from "./components/Hello/hello";

// 创建并暴露app
export default class App extends Component {
    render(h) {
        return (
            <div>
                <Hello></Hello>
            </div>
        )
    }
}
