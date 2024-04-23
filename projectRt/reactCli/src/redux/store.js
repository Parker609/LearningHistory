// 用于创建redux的公共store，使用redux的方法；
import {legacy_createStore as createStore, applyMiddleware, combineReducers} from 'redux';
// createStore在未来会被弃用，后续建议使用redux toolkit来创建redux；
// redux toolkit其实就是针对redux的一层封装，毕竟工具好用就行，不需要太大的灵活度
import countReducer from './reducer';
// 引入redux-thunk，支持异步action；但是异步action并不常用；
import {thunk} from 'redux-thunk';
// 当遇到多个reducer并放在一个store中时，要使用combineReducers（将多个reducer融合）
// export const store = createStore(countReducer, applyMiddleware(thunk));
const allReducers = combineReducers({
    cnt: countReducer
});

export const store = createStore(allReducers, applyMiddleware(thunk));