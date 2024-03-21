import React, {Component} from "react";

import "./index.css"

export default class ContainerListItem extends Component {
    state = {
        isLight: false
    }

    lightChange = (i) => {
        this.setState({isLight: i})
        console.log(this.state.isLight)
    }

    render() {
        const {todo, listOperate} = this.props;
        const {isLight} = this.state;
    
        return (
            <div className={`item-wrapper ${isLight ? 'light' : 'not-light'}`} onMouseEnter={() => {this.lightChange(true)}} onMouseLeave={() => {this.lightChange(false)}}>
                <div>
                    <input type="checkbox" checked={todo.isDone} readOnly/>
                    <span>{todo.todo}</span>
                </div>

                <div className="btns">
                    <div className="finish" onClick={() => {listOperate('fin', {id: todo.id})}}>完成</div>
                    <div className="del" onClick={() => {listOperate('del', {id: todo.id})}}>删除</div>
                </div>
            </div>
        )
    }
}