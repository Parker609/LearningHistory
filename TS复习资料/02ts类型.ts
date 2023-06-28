// ts是一个静态类型语言，相当于把js的动态类型静态化了
// 类型赋予方法：let a:string = 'aaa'，以此方法来声明变量类型

// 1. 字符串类型
let str: string = 'hello';
// str = 1; // 会报错
str = 'hello too';

// 2. 数字类型num
let num: number = 123;

// 3. boolean
let bool: boolean = true;

// 4. 字面量，即用某个值来当作类型，相当于赋予一个const
let va2: "1231";
va2 = "1231"; // 只能等于这个歌值，相当于一个变量，不常用；

// 5. any，任意类型，相当于没设定
let anyVar: any;
anyVar = 1;
anyVar = 'string';
anyVar = false;

// 可以把any类型的值赋予类型，不安全的；
let str2: string;
str2 = anyVar; // 不报错，表示不安全；

// 6. unknown，表示未知类型，效果和any基本一样；
let unknownVar: unknown;
unknownVar = 1;
unknownVar = 'string';

// str2 = unknownVar; // 会报错，是安全的
// 所以，unknown类型的变量，就是一个安全的any类型

// ****类型断言*****
// 当编译器不确定类型，但是认为可以认定类型时，可以解决这个报错
str2 = unknownVar as string; // 不报错，断言这玩意就是个string类型；
str2 = <string>unknownVar; // 不报错，断言这玩意就是个string类型；用泛型来处理；

// 7. void，表示函数没有返回值
function foo():void {
    // return 123; // 会报错
};

// 8. never，肯定不会有返回值，undefined都没有，类似于报错放过发
function foo2():never {
    throw new Error('报错了');
}