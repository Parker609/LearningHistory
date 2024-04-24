import React, { Component, lazy, Suspense } from 'react';
import {BrowserRouter, NavLink, Route} from 'react-router-dom'; // 引入路由组件

// 使用lazy懒加载组件；需要用suspense来包裹一下；
const T = lazy(() => import('./testLazy'));

export default class LazyLoad extends Component {
  render() {
    return (
      <div>
        <BrowserRouter>
            <NavLink to="1" children="123"/>
            {/* 懒加载的组件需要被suspense包裹 */}
            <Suspense fallback={<div>12312312</div>}>
                <Route path="/1" component={T}></Route>
            </Suspense>
        </BrowserRouter>
      </div>
    )
  }
}
