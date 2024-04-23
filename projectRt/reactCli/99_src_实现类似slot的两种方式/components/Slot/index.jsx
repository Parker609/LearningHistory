import React, {Component} from 'react';

export default class Count extends Component {
    state = {
        name: 223
    }
    render() {
        // 通过type可以获取到class圆形函数

        // console.log(this.props.getSlotModule())
        return (
            <div>
                {this.props.getSlotModule(this.state.name)}
            </div>
        )
    };
};

/**
 * slot的实现，其实就是在slot父组件中留一个空间，将传入的jsx补充在空间中；
 * 无论是通过children还是通过参数（传入object或者方法）的方式传入，都是为了满足上方的空间；
 * 如果要在子组件中添加slot中的内容（类似于作用域插槽），则以方法的形式传递进来（毕竟方法是可以携带参数的，而参数可以从内部传入）；
 */