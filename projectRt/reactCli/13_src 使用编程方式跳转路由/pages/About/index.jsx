import React, { Component } from 'react';

export default class About extends Component {
  // 利用props里history封装的api，可以实现用代码来控制跳转；
  // 必须是放在route组件里才行；
  
  // push = () => {
  //   this.props.history.push('/about/push')
  // }
  
  // 除了可以通过修改跳转链接来携带参数，还可以在后边传递state参数；
  push = () => {
    this.props.history.push('/home', {a: 12, b: 29})
  }
  replace = () => {
    this.props.history.replace('/about/replace')
  }
  render() {
    return (
      <div>
        this is About;
        <div className="btn" onClick={this.push}>更改路由为about/push</div>
        <div className="btn" onClick={this.replace}>更改路由为about/replace</div>
      </div>
    )
  }
}

/**
 * 除此以外，history里边还有go、goForward、goBack等方法，可以调用浏览历史；
 */