// 定义一个类：class关键字
// 构造函数关键字：
var Person = /** @class */ (function () {
    function Person() {
        // 表示类里边的只读属性；其实就是类似const
        this.gender = 'male';
    }
    // 方法
    // 相当于：syaHello: function(){}，简写，语法糖
    Person.prototype.sayHello = function () {
        console.log('hello');
    };
    // 以static开头，则是静态方法
    Person.sayHello2 = function () {
        console.log('hello2');
    };
    // 静态属性，static关键字，其实就是类属性
    Person.maxHeight = 2.30;
    return Person;
}());
var per = new Person();
console.log(per.age);
// 
console.log(Person.maxHeight);
per.sayHello();
Person.sayHello2();
