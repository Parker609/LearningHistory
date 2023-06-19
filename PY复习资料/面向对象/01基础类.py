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
    def __init__(self) -> None:
        pass
    
    # 对象的方法
    def bark(self):
        print('bark')

ani = Ani()
ani.bark()
print(ani.name)

"""
    二、类的属性和方法
        1. 属性：静态属性、对象属性；
"""