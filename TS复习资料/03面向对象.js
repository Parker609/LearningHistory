// 定义一个类：class关键字
// 构造函数关键字：constructor：在函数实例化时调用
// this关键字，一般指向实例化对象；
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
