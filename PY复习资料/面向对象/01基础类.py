
"""
    类：是面向对象思想的实现，封装、继承、多态
"""

"""
    一、类的简单定义：class
"""
# 简单定义一个动物类，创建之后再实例化它；
# python的对象实例化竟然不需要new，不用new关键字；

class Ani:
    # 对象的属性
    name = "cat"
    # 在python3.5增加了返回值类型，算是提高了代码的可读性，降低了阅读难度；
    # 类里边有很多的内置函数，如__init__(self)，是类的构造函数，当实例化的时候会自动调用，可以用于给对象的属性赋值；
    # 类中的函数的第一个入参是self，默认将实例对象传入；此值非占用字段，可以将值自定义；

    def __init__(self) -> None:
        pass
    
    # 对象的方法
    def bark(self):
        print(f'bark{self.__age}')

# ani = Ani()
# ani.bark()
# print(ani.name)

"""
    二、类的各种属性和方法详解
        1. 普通属性：变量定义即可
        2. 私有属性：__变量名（双下划线+变量名），外部不可以调用
        3. 静态属性：@property装饰器装饰的方法，此静态属性其实就相当于C#里的属性，可以写getter和setter以及deleter；
        4. 普通方法：def + 方法名
        5. 类方法：@classmethod装饰的，和普通方法很相似，可以给实例对象使用；约定是类专用的；
        6. 静态方法：@staticmetod装饰，不用传self字段，是约定给类用的；
"""

class Ani:
    # 普通属性
    name = 'name'
    # 私有属性
    __age = 18
    # 私有方法，外界不能调用，只能是内部自己调用；
    def __say_hello(self):
        print("say hello")
    # 静态属性：通过getter和setter把私有属性保护起来了
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, val):
        # set age的时候会调用
        self.__age = val
    @age.deleter
    def age(self):
        print("age被删除的时候调用的")

    # 类的普通方法
    def say(self):
        print("喵喵喵~")

    @classmethod
    def bark(cls):
        print("汪汪汪")
    @staticmethod
    def sleep():
        print("Zzzz……")
    
ani = Ani()
print(ani.name)
# print(ani.__age) # 'Ani' object has no attribute '__age' 报错
# ani.__say_hello() # 'Ani' object has no attribute '__say_hello' 报错
ani.age = 21
age = ani.age # 获取age的时候使用的
print(age)
# del ani.age 删除ani里的age时使用
ani.say()
ani.bark() # 实例用也是可以用的
Ani.bark() # 类是这么用的，其实这个装饰的不知道有啥用

ani.sleep() # 也能用，不过不建议这么用
Ani.sleep() # 约定是类的方法，给类直接使用的；

# python的类结构很像js的，原型链的方法沿用下来的；这边感觉所有的类其实都是原型链的方法沿用下来的；

"""
    三、魔法函数：class内置了一些函数，和生命周期函数类似，勇敢与增强一个类的特性，写法是__函数名__（magic function）
        1. __repr__：用于命令行模式，实例化class之后，可以通过在命令行给中输入实例的名称来执行的；
        2. __init__：class中最通用的命令行，class实例化之后会首先调用的，算是初始化函数，也可以被称作构造函数；
        3. __str__：打印某个实例的时候就会调用；
        …… ……
        反正有很多，后续用到的话可以查，并且当执行某个操作的时候，其实就是调用这个对象里的魔法函数，比方说abs，求绝对值，其实就是调用这个对象的魔法函数；
"""

class Test:
    def __str__(self) -> str:
        return "thsi is class test"
    
    def __abs__(self):
        return 111
    
test = Test()
print(test)

print(abs(test))

# 所以这块说python是面向对象的语言，因为python里边基本上所有都是一个个对象