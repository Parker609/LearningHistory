import React, {useState, useEffect} from "react"

// 方法其实就相当于类式组件的render；
export default function(props) {
    // 常用hooks之一：useState；
    const [count, setCount] = useState(0);
    // state值和重新设定值的方法；
    const add = function () {
        // setCount(count + 1)
        // setCount可以放方法，将返回值赋予state，入参是当前的state；
        setCount(a => a + 1)
    }

    // 常用hooks之二：useEffect
    // useEffect，翻译过来是副作用，可以用于模拟生命周期；
    // useEffect本身用法是初始化调用一次，后续用于监听输入的state，返回值用于willUnmounted；
    useEffect(() => {
        // count每次更新都要调这个方法；
        console.log('@')
        return () =>  {
            // 卸载之前调用一次；
            console.log('没了')
        }
    }, [count])
    // 若第二个参数不输入，则认为监听所有的state值，所以会实现render一样的调用顺序；
    return (
        <div>
            <div>{count}</div>
            <div onClick={add}>Hooks</div>
        </div>
    )
}