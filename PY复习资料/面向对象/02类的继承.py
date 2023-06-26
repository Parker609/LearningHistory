"""
    一、简单实现一个继承：通过类名(父类类名)的书写方法
"""

class Ani:
    name = '汪汪'

    def roar(self):
        print("Roar")

class Dog(Ani):
    pass

dog = Dog()
# dog.roar()

"""
    二、父类的基本上所有方法都能继承过来
"""
class Ani:
    # 普通属性
    name = 'name'
    # 私有属性
    __age = 18
    # 静态属性：通过getter和setter把私有属性保护起来了
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, val):
        print("调用赋值的时候会被调用")
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

class Dog(Ani):
    pass

dog = Dog()
cat = Ani()

dog.age=19
print(dog.age)
dog.say()
dog.sleep()
Dog.sleep()

"""
    三、当父类有构造函数的时候，要注意用super执行一下，否则父类的赋值就不在了；
"""

class Ani:
    name = ''
    def __init__(self, name) -> None:
        self.name = name
    def bark(self):
        print(self.name)

class Dog(Ani):
    def __init__(self, name) -> None:
        # 没有这个super会报错的；除非不写这个init
        super().__init__(name)

dog = Dog('xh')
print(dog.name)

# super详解，其实是相当于执行了父类的的构造函数，其实super是一个类方法的简写，其实是执行了super(Dog, self).init('xh')
class Dog(Ani):
    def __init__(self, name) -> None:
        # 没有这个super会报错的；除非不写这个init
        super(Dog, self).__init__(name)

dog = Dog('xh')
print(dog.name) # 输出效果一样，意思是从self的父类队列里，找到Dog后边的那个父类并返回，并将self作为对象传入，执行init方法；
# 这样说，super可以用的地方也比较多，可以当js里的call来用了；
# 例如


super(Dog, dog).__init__('xxx')
print(dog.name)

# 注意，这块的dog须是前边的那个类的实例

"""
    Python的继承是支持多继承的，即一个子类可以有多个父类：
        1. 语法：class A(B, C, D):
        2. 看Python版本，高版本Python是宽度优先的，低版本是广度优先的
"""

class A:
    def __init__(self) -> None:
        self.say()

    def say(self):
        print("this is A")

class B:
    def __init__(self) -> None:
        self.say()
        
    def say(self):
        print("this is B")

class C:
    name = ''
    def __init__(self, name) -> None:
        self.name = name
        self.say()

    def say(self):
        print("this is C")

class D(A, B, C):
    pass

# 在多继承时，如果子类没有构造函数，则直接继承第一个父类的构造函数；
a = D()

class E(A, B, C):
    def __init__(self) -> None:
        print("this is E")
        # super 会调用第一个父类的构造函数，其余的构造函数就不调用了
        super().__init__()
e = E()
print(e.name) # 构造函数没有处理，很可惜；
# 总而言之，不建议使用多继承；代码的可读性太差了

"""
    Python 多继承，是有继承顺序的，最新的Python里是广度优先的，即：
        B, C 都继承自A，D继承自B和C，那么会优先继承B和C的，在找A的；
"""

class A:
    def say(self):
        print("this is A")
        
    def say2(self):
        print("this is A")

    def say3(self):
        print("this is A")

class B(A):
    a = 100
    def say(self):
        print("this is B")

class C(A):
    a = 200
    def say(self):
        print("this is C")

    def say2(self):
        print("this is C")

class D(B, C):
    @property
    def get_num(self):
        # 这种写法相当于把C类中的a当成静态属性了
        return C.a

d = D()
d.say() # 先执行B，因为B在前边
d.say2()
d.say3() # 一层一层的找，666

C.a =3000
c = C()
print(c.a) # 不建议用静态属性；即类属性；

print(d.get_num)