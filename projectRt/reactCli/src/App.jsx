// 创建app
import React, {Component} from "react";
// import应用的组件
import Header from "./components/Header";
import Container from "./components/Container";

// 创建并暴露app
export default class App extends Component {
    state = {
        todos: [
            {id: 0, todo: '吃饭', isDone: true},
            {id: 1, todo: '刷牙', isDone: false},
            {id: 2, todo: '睡觉', isDone: false}
        ]
    }
    finish = (id) => {
        const newTodos = this.state.todos.map(item => {
            return {
                ...item,
                isDone: item.isDone || +item.id === +id
            }
        });
        this.setState({todos: newTodos})
    }
    del = (id) => {
        const newTodos = this.state.todos.filter(item => {
            return item.id !== id;
        });
        this.setState({todos: newTodos})
    }
    addIntoTodos = (val) => {
        const {todos} = this.state;
        todos.unshift({
            id: Date.now(),
            todo: val,
            isDone: false
        });
        this.setState({todos})
    }
    render(h) {
        const {todos} = this.state;
        return (
            <div>
                <Header addIntoTodos={this.addIntoTodos}></Header>
                <Container todos={todos} finish={this.finish} del={this.del}></Container>
            </div>
        )
    }
}
