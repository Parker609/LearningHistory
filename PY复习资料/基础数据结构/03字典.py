"""
    本节的内容是字典，即{}，dict，对标js里的object，对象；
"""

"""
    一、字典的创建方法
        1. 用{}创建，最为简单；
        2. 使用dict创建；
        3. 使用zip打包，将两个list合并在一起；
        4. 使用dict.fromkeys来创建；
        
"""

# 1. 直接用花括号创建简单的字典
dic = {'name': 123} # 这块要注意，key值必须是字符串，weakmap
print(dic)

# 2. 使用dict创建
dic = dict(name='张', age='19')
print(dic)

# 3. 使用zip打包
print(dict(zip(['1', '2', '3'], [4, 5, 6])))

# 4. 利用list的值创建空字典
print(dict.fromkeys(['1', '3', '14']))

"""
    二、字典中元素的访问
        1. 通过键值对，如果没有这个值，直接抛出异常
        2. 使用get方法，若键值对不匹配，返回None
        3. 通过字典的items方法，来输出所有的键值对
        4. 列出所有的值：keys和values
        5. 字典长度：len()
"""
# 1. 通过键值对
print(dic['name'])

# 2. 通过get方法
print(dic.get('name'))

# 3. 字典的items，相当于js里的enties属性；
print(dic.items())

# 4. 列出所有的
for i in dic.values():
    print(i)

# 5. 获取字典长度
print(len(dic))

"""
    三、字典中添加元素
        1. 键值对覆盖
        2. 用updata合并两个dic
"""

# 1. 通过键值对来赋值
dic['height'] = 123
print(dic['height'])

# 2. 通过updata
temp_dic = {'name': 'zs', 'age': 13}
dic.update(temp_dic)
print(dic['age'])

"""
    四、删除字典中的某个元素
        1. del方法；删除某一个
        2. clear方法；清空字典
        3. pop方法，删除某个键，返回某个值；
        4. popitem，删除最后一个值，但是在3.7版本之前是删除某个随机值；
"""

temp_dic = {'name': 'zs', 'age': 13, 'height': 180, 'grade': 3}

# 1. del方法
del(temp_dic['age'])
print(temp_dic)

# 2. pop方法，没有对应的key则会报错
pop_member = temp_dic.pop('name')
print(pop_member)
print(temp_dic)

# 3. popitem方法，吐最后一个值，（字典还有顺序么）
temp_dic = {'name': 'zs', 'age': 13, 'height': 180, 'grade': 3}
pop_member = temp_dic.popitem() # 没有参数
print(pop_member)
print(temp_dic)

# 4. 清空整个列表，一般情况下直接 = {} 这样其实用起来更方便；不过如果这块有传址的操作，想清空所有，还是要用clear；
temp_dic2 = temp_dic
temp_dic.popitem()
print(temp_dic)
print(temp_dic2)
temp_dic.clear()
print(temp_dic)
print(temp_dic2)

"""
    五、序列解包，解构赋值。
        1. 其实这块是用到的列表的解构赋值，a,b,c = [1,2,3]， 会将123复制给abc，这块的字典没有解构操作
"""
temp_dic = {'name': 'zs', 'age': 13, 'height': 180, 'grade': 3}
print(temp_dic.keys())
a,b,c,d = temp_dic.keys() # 这块不能有空格，这样用对格式要求太高了，还是用普通的取值方法就行；
print(a)

