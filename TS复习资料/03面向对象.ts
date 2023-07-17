// 定义一个类：class关键字

class Person {
    // 静态属性，static关键字，其实就是类属性
    static maxHeight: number = 2.30;

    // 定义属性
    name: string;
    age: number;

    // 表示类里边的只读属性；其实就是类似const
    readonly gender: string = 'male';

    // 方法
    // 相当于：syaHello: function(){}，简写，语法糖
    sayHello() {
        console.log('hello')
    }

    // 以static开头，则是静态方法
    static sayHello2() {
        console.log('hello2');
    }
}

const per:Person = new Person();
console.log(per.age)
// 
console.log(Person.maxHeight)

per.sayHello();

Person.sayHello2();