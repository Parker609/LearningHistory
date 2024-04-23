import React, {Component} from "react";
import SlotWrapper from './components/SlotWrapper';
import Test from './components/Test';
import Slot from './components/Slot';

export default class App extends Component
{
    render() {
        return (
            <div>
                <SlotWrapper>
                    <Test></Test>
                </SlotWrapper>
                {/* 不通过children的方式创建slot */}
                <Slot getSlotModule={name => <div>12312</div>}>

                </Slot>
            </div>
        )
    }
}