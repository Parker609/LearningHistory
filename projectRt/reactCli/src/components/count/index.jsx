import React, {Component} from 'react';
import {store} from '../../redux/store'
const a = 124;

export default class Count extends Component {
    componentDidMount() {
        console.log(123);
        // 第一个redux api：getState，获取当前状态；详情可见render
        // 第二个api：subscribe，订阅事件，当store每次更新都会唤起；
        store.subscribe(() => {
            console.log('store的state变了');
            this.setState({})
        });
    };
    state = {
        count: 12
    };
    increaseOne = () => {
        // 第三个redux api：dispatch，发出一个action；
        // this.setState({count: this.state.count + 1})
        store.dispatch({type: 'increase', data: 1})
    };
    render() {
        const {count} = this.state;
        return (
            <div>
                <div>
                    this count is {count} {store.getState()}
                </div>
                <div>
                    <button onClick={this.increaseOne}>+1</button>
                </div>
            </div>
        )
    };
}

/**
 * redux在定义好store之后，可以通过getState来获取当前的值；
 * 但是当前值通过dispatch方法出发reducer更新后，并不会自动触发render来重新渲染；
 * 因此一般需要通过subscribe来获取当前已经改变的值；并通过setState来触发页面的重新渲染；
 */