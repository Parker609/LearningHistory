import React, {Component} from "react";
import "./index.css";

export default class Header extends Component {
    render() {
        return (
            <div>
                <input onKeyDown={this.keyDown} className="header-input" type="text" placeholder="清输入，点击回车保存数据"/>
            </div>
        )
    }
    
    keyDown = (e) => {
        const {addIntoTodos} = this.props;
        if (e.key === 'Enter') {
            addIntoTodos(e.target.value)
        }
    }
}