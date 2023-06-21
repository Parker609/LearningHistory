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