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