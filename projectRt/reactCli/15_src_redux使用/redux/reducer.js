// 用于创建redux的参数处理工具reducer
import { INCREASEMENT } from "./type";

// reducer由两个入参：preState以及action：preState标识之前的状态，action标识动作
// action包含两个数据，分别是type（动作类型）data（动作数据）如（+）（1）
export default function countReducer (preState, action) {
    const DEFAULT_STATE = 0;
    const {type, data} = action;
    switch(type) {
        case INCREASEMENT:
        // 若return和prestate相等，则不触发store的sub方法；仅作浅层的比较；
            return preState + data;
        // default场景表示第一次获取，毕竟没有任何操作的情况下，那就是默认值了；
        default:
            return DEFAULT_STATE;
    }
};