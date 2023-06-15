"""
    类：是面向对象思想的实现，封装、继承、多态
"""

"""
    一、类的简单定义：class
"""
# 简单定义一个动物类，创建之后再实例化它；
# python的对象实例化竟然不需要new，不用new关键字；

class Ani:
    def __init__(self) -> None:
        pass

    def bark(self):
        print('bark')

ani = Ani()
ani.bark()