import React, {Component} from 'react';
import {connect} from 'react-redux';
import {countActionIncrease} from '../../redux/actions'

class Count extends Component {
    increaseOne = () => {
        this.props.increase(1)
    };
    render() {
        const {cnt} = this.props;
        return (
            <div>
                {cnt}
                <div>
                    <button onClick={this.increaseOne}>+1</button>
                </div>
            </div>
        )
    };
}

export default connect(
    state => ({cnt: state}),
    {
        increase: countActionIncrease
    }
)(Count);

/**
 * react-redux，facebook推出的专门操作redux的封装；
 * 很多需要自己操作的均封装在里边了；
 * 
 * react-redux将组件分成了两类：UI组件和容器组件；容器组件由react-redux库提供；
 * 将当前的状态以及操作redux的方法传入即可；
 * 
 * 数据的刷新也不需要人工操作，都交给容器组件处理了；
 */