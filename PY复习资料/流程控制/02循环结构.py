# 和其他语言一样，循环要设置推出条件，不能无线循环；
# 循环结构第一种 while
"""
    while 表达式：
        循环体
"""

condition = 10
while condition:
    # print("111")
    condition -= 1
    # print(condition)

# 第二种循环 for循环
"""
    for 迭代变量 in 迭代体（字符串、列表、元组、字典、集合）:
        循环体
"""

# 一般不用for i = 1, i < n, i ++ 这种，迭代变量直接代表迭代的内容，所以在控制循环多少遍的时候，一般会用到range 和 len方法，比如；
# 循环10遍，其中的range是左闭右开，相当于[0, 10)，生成一个0~10的列表
for i in range(10):
    print(i)

for i in "this is a a a a ":
    print(i)

"""
    关键字：和其他代码是一样的，没啥好说的
        1. continue：结束这次循环，进入下次循环
        2. break：退出这次循环，进入下次循环
        3. return：结束所有循环，直接返回结果
        4. pass：占位符，没有啥大用，就是记录这块有代码没写，不加pass会报错；
"""