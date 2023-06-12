"""
    本节讲述list，即列表，也被称作可变序列
"""

"""
    一、列表的创建
        1. 直接使用中括号创建；
        2. 使用list创建；
        3. 用range方法创建数列；
        4. 用列表推导式创建；
"""
# 1. 使用中括号创建
from asyncio import constants


print([1, 2, 3])

# 2. 使用list创建
print(list('abcd')) # 直接将字符串拆开

# 3. 使用range创建数组
print(list(range(1, 100, 2))) # 需要通过list方法将range给强制转换一下

# 4. 列表表达式，其实就是在列表里写个循环
print([i for i in range(1, 10 ,2)])
# [print(1) for i in range(1, 19, 2)] 列表的特殊写法，循环的第一个可以是表达式

"""
    二、列表中添加内容
        1. append方法，在队列结尾添加某个元素，修改原数组，无返回值
        2. extend方法，在队列的后边链接某个数组，改变原数组
        3. insert方法，在指定位置插入某个数组，相当于splice
        4. + * 可以用来扩展数组，数组加和相当于extend，成法相当于多个extend相加和，创建了新的地址，所以不建议使用
"""
# append
l = [1, 2]
l.append(3)
print(l)

# extend
l.extend([22,2])
print(l)

# insert
l.insert(1, 1999)
print(l)

l = l + [1231321] # 有返回值，加和
print(l)

"""
    三、列表删除
        1. pop，根据索引弹出某个值，默认弹出结尾的值
        2. del，删除指定位置的值，若不加索引，则删除整个列表
        3. remove，输入要删除的值，去除首次出现的这个值
        4. clear，清楚整个列表里的值，但是保留列表
"""

# del方法

del l
# print(l) 会报错

# pop方法

l = [1, 1, 2, 3, 4]
p = l.pop()
print(l)

# remove方法
l.remove(1)
print(l)

# clear方法
l.clear()
print(l)

"""
    四、获取列表中其余的方法
        1. index，输出第一个值所在的索引位置
        2. count，获取列表中指定数据出现次数
        3. len，用来获取列表的长度
        4. sort，排序，默认顺序排序
        5. reverse，反转数组
        6. 判断某个值是否在数组中，可以用in
"""
l = [1, 1, 2, 3, 4]


# index
print(l.index(1))

# count
print(l.count(1))

# len
print(len(l))

# reverse
l.reverse()
print(l)

# sort
l.sort()
print(l)
l.sort(reverse=True)
print(l)

"""
    五、切片语法，和string是一样的
"""
# 通过切片语法获取新的数组，reverse效果
l = [1, 2, 3, 4, 5]

print(l[::-1])
print(l) # 不影响原数组

# 通过切片更换数组里的值，值可以多也可以少
l[1:3] = [5, 5, 5, 7]
print(l)

"""
    六、列表内置函数汇总，以下值都有返回值
        1. max，列表中的最大值
        2. min，列表中的最小值
        3. sum，列表求和
        4. sorted，列表排序，默认从小到大
"""
# max
print(max(l))
print(min(l))
print(sum(l))
print(sorted(l))

"""
    七、列表遍历，for循环以及while，没有do while
"""

l = [1,2,3,4,5,5,5,5,5,5,2]
for i in l:
    print(i)

i = 0
while i < len(l):
    print(l[i])
    i += 1

"""
    八、列表表达式，列表里可以嵌套for循环
        1. 列表表达式，需要从后往前看
        2. in
"""
l2 = [i for i in range(1, 10, 2) if i not in [3, 4, 5]]
print(l2)

"""
    九、深拷贝和浅拷贝
        1. python里的深拷贝和钱拷贝和正常js之类的深拷贝和浅拷贝是不一样的；
        2. 其余的深浅拷贝只是只传值和传址的关系
        3. python真的是深浅，copy和deepcopy
        4. 对于浅拷贝，其实就是浅层的深拷贝
        5. 深拷贝就是深层的深拷贝
"""

test_list = [[1,2], [3, 4], 5]
test_list2 = test_list.copy()
# 上边的方法也可以写成copy.copy()；
test_list[2] = 10

print(test_list)
print(test_list2) # 此时，list2是不变的

test_list[0].append(12)
print(test_list)
print(test_list2) # 此时，list2里的索引为0的数组发生了改变，即二者的id是一样的
print(id(test_list[0]))
print(id(test_list2[0]))
# test_list[0].append(123)
# print(test_list2)

# 深拷贝就是对象里的子对象的地址也是变化的
import copy

test_list = [[1,2], [3, 4], 5]
test_list2 = copy.deepcopy(test_list)
print(id(test_list[0]))
print(id(test_list2[0]))

"""
    十、注意内容
        1. 列表里可以是任意数据类型，即any
        2. 列表的长短可变，相当于c#中的list，js的array
"""

"""
    PS、元组：元组可视为List的一种，是一种不可变序列；支持索引、切片、遍历等操作；
"""

"""
    PS、元组的定义：
        1. 元组的定义相较于List，其实就是用()来标注；
        2. 当元组中只有一个元素时，可以在元素后边加一个『,』，来标识是元组，否则python会认为这个是一个单字符
"""

print(type((3))) # int
print(type((3,))) # tuple

# 用tuple定义
print(tuple([1,2,3]))

"""
    PS、元组的计算：
        1. 加法：合并两个元组;
        2. 乘法：元组重复
        3. in：数字是否在元组中
        4. is：两个元组是否是一个地址
        5. ==：两个数组是否一样
        6. > <：两个元组大小对比；
"""

temp_tup = (1, 2, 5)
# 1. 加法
print(temp_tup + temp_tup)
# 2. 乘法
print(temp_tup * 3)
# 3. in（对比的是地址）
print(5 in temp_tup)
# 4. is
print((1, 2, 5) is temp_tup)
print(id((1, 2, 5)))
print(id(temp_tup))
# 5. ==
print((1, 2, 3) == (1, 2, 3))

# Python中的==等号应用，这块说的都是对比值，并不是直接地址对比；

"""
    PS、元组也支持索引切片、遍历
"""
# 1. 切片
temp_tup = (1, 2, 3, 5, 6)
print(temp_tup[3::-1])

# 2. 遍历
for i in temp_tup:
    print(i)

# 3. 支持count和index方法，用于
print(temp_tup.count(1))
print(temp_tup.index(3))

"""
    PS、元组存在的意义
        元组作为一个不可变序列，是保证数组在程序运行过程中，不会由于各种原因修改了数据，可以保证数据的完整性；
"""
