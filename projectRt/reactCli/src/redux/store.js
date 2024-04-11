// 用于创建redux的公共store，使用redux的方法；
import {legacy_createStore as createStore} from 'redux';
// createStore在未来会被弃用，后续建议使用redux toolkit来创建redux；
// redux toolkit其实就是针对redux的一层封装，毕竟工具好用就行，不需要太大的灵活度
import countReducer from './reducer';

export const store = createStore(countReducer);