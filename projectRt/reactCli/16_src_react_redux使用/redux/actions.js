import { INCREASEMENT } from "./type";
import { store } from "./store";

// redux的action生成

// 增加的action；
export const countActionIncrease = function (data) {
    return {type: INCREASEMENT, data};
};

// action一般是object或者函数，object则称为同步anction，否则称为异步action；

// 创建异步action
export const countAsyncActionIncrease = function (data) {
    return () => {
        setTimeout(() => {
            store.dispatch(countActionIncrease(data))
        }, 1000)
    }
}