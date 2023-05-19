"""
    本节的内容是字典，即{}，dict，对标js里的object，对象；
"""

"""
    一、字典的创建方法
        1. 用{}创建，最为简单；
        2. 
        
"""

# 1. 直接用花括号创建简单的字典
dic = {'name': 123} # 这块要注意，key值必须是字符串，weakmap
print(dic)

# 2. 使用dict创建
dic = dict(name='张', age='19')
print(dic)

# 3. 使用zip打包
print(dict(zip(['1', '2', '3'], [4, 5, 6])))