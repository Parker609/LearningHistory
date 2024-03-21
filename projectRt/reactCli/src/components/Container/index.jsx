import React, {Component} from "react";
import ContainerListItem from "../ContainerListItem"

export default class Container extends Component {
    listOperate = (type, params) => {
        const {finish = () => {}, del = () => {}} = this.props;
        const {id} = params;
        switch(type) {
            case 'fin':
                // 执行已完成操作
                finish(id);
                break;
            case 'del':
                // 执行删除操作
                del(id);
                break;
            default:
                break;
        }
    }
    render() {
        return (
            <div>   
                {
                    this.props.todos?.map(item => {
                        return (
                            <div key={item.id}>
                                <ContainerListItem todo={item} listOperate={this.listOperate}/>
                            </div>
                        )
                    })
                }
            </div>
        )
    }
}