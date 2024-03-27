import React, { Component } from 'react'

export default class index extends Component {
  render() {
    console.log(this.props.match.params)
    // 在match属性中，可以接收到传递进来的值；
    // 但是这种方法不打友好：1：默认redirect不会有任何参数传递进来；2：占用了路由
    return (
      <div>
        this is Home
      </div>
    )
  }
}
