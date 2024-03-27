import React, { Component } from 'react';
import { NavLink } from 'react-router-dom';

// 作为一个封装好的link;
// 组件标签中间的内容会作为props里特殊的children属性传入；
// 当然，若直接给组件设定childre属性，会直接填充标签中间的内容；
// 即<div children="11"></div> === <div>11</div>；
// 后者<div>11</div>里的11，其实算是一种特殊的标签属性；
// 自定义组件设置children时，会被传入，而不会生效；

export default class Idx extends Component {
  render() {
    return (
        <NavLink activeClassName="test-active" {...this.props}/>
    )
  }
}
