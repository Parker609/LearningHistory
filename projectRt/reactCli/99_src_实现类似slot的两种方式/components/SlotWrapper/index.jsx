import React, {Component} from 'react';

export default class Count extends Component {
    render() {
        // 通过type可以获取到class圆形函数
        const C = this.props.children.type;
        return (
            <div>
                <C a={1231}></C>
            </div>
        )
    };
};