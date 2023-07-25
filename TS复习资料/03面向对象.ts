// 定义一个类：class关键字
// 构造函数关键字：constructor：在函数实例化时调用
// this关键字，一般指向实例化对象；

class Person {
    // 静态属性，static关键字，其实就是类属性
    static maxHeight: number = 2.30;

    // 定义属性
    name: string;
    age: number;

    // 表示类里边的只读属性；其实就是类似const
    readonly gender: string = 'male';

    // 构造函数方法
    constructor(name: string, age: number) {
        this.name = name;
        this.age = age;
    }
    // 方法
    // 相当于：syaHello: function(){}，简写，语法糖
    sayHello() {
        console.log('hello')
    }

    // 以static开头，则是静态方法
    static sayHello2() {
        console.log('hello22');
    }
}

const per:Person = new Person('zs2', 18);

// 输出age
console.log(per.age, 'console')
// 输出maxHeight， readonly
console.log(Person.maxHeight)
// 输出姓名
console.log(per.name, 'consolename')
per.sayHello();

Person.sayHello2();

// 继承

// 定义一个Ani的类
class Ani{
    name: string;
    age: number;

    constructor(name:string, age: number) {
        this.name = name;
        this.age = age;
    }

    sayHello() {
        console.log('sayHello');
    }
}

// 继承关键字：extends，和js基本一样
// 面相对象的原理已经看了好多遍呢了，就不追书了
class Dog extends Ani{

}

// 直接执行了父类的初始化方法，在python中是不执行的；
const dog = new Dog('zs', 22);
console.log(dog.name)