// 创建app
import React, {Component} from "react";

// 创建并暴露app
export default class App extends Component {
    render() {
        return (
            <div>
                123
            </div>
        )
    }
}

/**
 * 接下来讲解前端路由
 * 前端路由其实是依赖于BOM上的History对象来操作的，包括pushState和history的listen事件。
 * 相对于history的控制，hash的兼容性会更好，因为部分老的浏览器不支持用户手动修改history。
 */
