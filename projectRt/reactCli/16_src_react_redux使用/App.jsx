import React, {Component} from "react";
import Count from './components/count'
import {store} from './redux/store';
// store可以通过provider来批量处理（容器其实特别像插槽）
import { Provider } from "react-redux";

export default class App extends Component
{
    render() {
        return (
            <div>
                <Provider store={store}>
                    <Count store={store}/>
                </Provider>
            </div>
        )
    }
}