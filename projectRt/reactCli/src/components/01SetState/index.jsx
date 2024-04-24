import React, { Component } from 'react'

export default class SetState extends Component {
  state = {cnt: 0}
  triggerSetState = () => {
    // setState第一种写法：直接写，但是setState其实时异步的，也就是说在赋值之后再调用这个值，这个值其实还没变；
    // 也就是说，setState里，对值的覆盖，其实是在整次逻辑执行之后操作的；
    // 特别像是中间添加了一个setTimeout的操作，执行队列靠后了；
    // this.setState({cnt: this.state.cnt + 1}, () => {
    //   // 显然有个延迟；
    //   console.log(this.state.cnt, 'callbackConsole')
    // });
    // console.log(this.state.cnt, 'currentconsole'); // 其实是会打印成0的；

    // 若期望某些操作是在setState之后执行，可以给setState后边添加回调；

    // setState的第二种写法：函数式，对象式的是函数式的语法糖；默认把state值传递进去；
    this.setState(state => {
      return {cnt: state.cnt + 100}
    }, () => {})
  }
  render() {
    return (
      <div onClick={this.triggerSetState}>
        <div>{this.state.cnt}</div>
        SetState...
      </div>
    )
  }
}
