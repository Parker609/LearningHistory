import React, { Component } from 'react'
import { withRouter } from 'react-router-dom'

class Header extends Component {
    componentDidMount() {
        console.log(this.props, 'header')
    }
    render() {
        return (
            <div>
                this is header
            </div>
        )
    }
}

// 如果希望一般组件也能由路由组件，类似history之类的属性方法，可以引入withRouter方法；
// 通过withRouter来装饰原油的class，在以达到能在实例的props属性上增加history等api
export default withRouter(Header)
