// ts是一个静态类型语言，相当于把js的动态类型静态化了
// 类型赋予方法：let a:string = 'aaa'，以此方法来声明变量类型

// 变量和函数都可以定义变量类型

let a:string = '12';
function foo3():string {
    return '1231';
}

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

// 9. object，对象的类型一般不用object，一般是用于指定对象中包含的属性
let obj: {name: string, age: number};
obj = {name: 'zs', age: 13}; // 结构必须和后边的类型一样

let obj2: {name: string, age: number, height?: number};
obj2 = {name: 'zs', age: 13}; // ；属性名后边添加问号，表示属性是可选的；？表示属性是可选的，可选属性

let obj3: {name: string, [prop: string]: any};
obj3 = {name: 'zs', age: 13, height: 24, graduated: false}; // [prop: string]: any，后边可以添加任意的值；

let foo4: (a: string, b: number) => string; // 使用箭头函数的方法来规定函数的格式；

// 9. 数组，最好是数组中仅存储单一类型的值；
let arr: string[];
arr = ['1', '2'];

let arr2 = Array<number>; // 效果差不多；

// 10. 元组，就是固定长度的数组；
let tp:[string, string];
tp = ['1', '2'];

// 11. enum，枚举
enum gender {
    Male,
    Female
};

let gd: gender;
gd = gender.Male;
gd = gender.Female; // 都一样

/**
 * 关键字： |：表示一个变量可以同时是a类性，也可使是b类性；
 *          &: 表示同时，用的比较少，常用在object中；
 *          类型的别名： type，用于表示创建一个类型的别名；
 */

let abc: string | number;
abc = 'zs';
abc = 123; // 都可以

// 类型的别名，简化类型的使用；
type myType = string | number;
let d: myType;
d = 'sdd';
d = 1231233;