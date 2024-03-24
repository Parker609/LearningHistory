// 创建app
import React, {Component} from "react";
import axios from 'axios';

// 创建并暴露app
export default class App extends Component {
    componentDidMount() {
        // 在加载的时候，访问serve请求数据；
        axios('http://localhost:3000/api/test').then(
            res => {console.log(res, 'consoleres')},
            err => {console.log(err, 'consoleerr')}
        )
    }
    render() {
        return (
            <div>
                123
            </div>
        )
    }
}
