// 定义一个类：class关键字
// 构造函数关键字：constructor：在函数实例化时调用
// this关键字，一般指向实例化对象；
var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var Person = /** @class */ (function () {
    // 构造函数方法
    function Person(name, age) {
        // 表示类里边的只读属性；其实就是类似const
        this.gender = 'male';
        this.name = name;
        this.age = age;
    }
    // 方法
    // 相当于：syaHello: function(){}，简写，语法糖
    Person.prototype.sayHello = function () {
        console.log('hello');
    };
    // 以static开头，则是静态方法
    Person.sayHello2 = function () {
        console.log('hello22');
    };
    // 静态属性，static关键字，其实就是类属性
    Person.maxHeight = 2.30;
    return Person;
}());
var per = new Person('zs2', 18);
// 输出age
console.log(per.age, 'console');
// 输出maxHeight， readonly
console.log(Person.maxHeight);
// 输出姓名
console.log(per.name, 'consolename');
per.sayHello();
Person.sayHello2();
// 继承
// 定义一个Ani的类
var Ani = /** @class */ (function () {
    function Ani(name, age) {
        this.name = name;
        this.age = age;
    }
    Ani.prototype.sayHello = function () {
        console.log('sayHello');
    };
    return Ani;
}());
// 继承关键字：extends，和js基本一样
// 面相对象的原理已经看了好多遍呢了，就不追书了
var Dog = /** @class */ (function (_super) {
    __extends(Dog, _super);
    function Dog() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    return Dog;
}(Ani));
// 直接执行了父类的初始化方法，在python中是不执行的；
var dog = new Dog('zs', 22);
console.log(dog.name);
