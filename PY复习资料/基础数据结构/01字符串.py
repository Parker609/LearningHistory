"""
    变量的命名规范：
        1. 一般是用小驼峰命名法，即：name_rule_first，所有字母小写，并且以下划线链接，被称作小驼峰命名法；
        2. python对字母大小写是敏感的，因此变量A和变量a是代表了不同的含义的；
        3. 和其他的语言一样，python自留字段

    python的注释：
        单行注释用 #，一般用ctrl+、来实现；
        多行注释用三个双引号，这种用法也可以用来给变量赋多行的字符串的值，一般在书写sql的时候使用；
"""

"""
    字符串：string
"""

"""
    一、字符串创建有三种方式：
        1. 通过单引号和双引号来创建字符串，一般情况下，在python中的字符串是使用双引号"字符串"来创建的，也可以用单引号来创建字符串'字符串'；
        2. 通过连续三个双引号来创建多行字符串；
        3. 空字符串也是字符串，算是长度为0的特殊字符串；
"""

# quote_string = "字符串"
# single_quote_string = '字符串'
# long_string = """
#     这是一串非常长的字符串
#     其中还包涵了换行
# """
# zero_len_string = ""
# print(quote_string, single_quote_string, long_string, len(zero_len_string))

"""
    二、常用的转义字符：
        1. \n 表示换行；
        2. \' 表示单引号作为字符输出；
        3. \t 制表符，相当于一个tab；
"""

"""
    三、字符串索引/切片
        1. python的字符串和list一样是有索引的，可以通过索引的方式对字符串进行选取和切片；
        2. 切片的格式是：字符串[起始索引:结束索引：步长]
        3. 举例：'12345'[1:4:2] ==> '24'
        4. 若步长为负数，则整个字符串倒序；有简写形式'123'[::-1]
"""
# print('12345'[1:4:2])
# print('12345'[1:4])
# 输出234，其实是[1,4)，左闭右开区间；
# print('123456'[::-1])

"""
    四、字符串的分割split方法
        1. 以split里的符号做标记，将左右分割，返回一个list；
        2. 若不输入参数，则认为输入了一个空白字符串，将以空白处作为分割，用的不多；
"""

print('123123,123123,22222'.split(','))
print('123 123'.split())

"""
    五、字符串的拼接
        1. 字符串的拼接常用方式有两种，分别是+和join方法；
        2. 从性能角度来看，join的性能要比+要好；
"""
test_str1 = 'this is a test'
test_str2 = 'this is test2'
print(test_str1 + test_str2)
# join的用法和js相反，前边的才是链接的字符，后边要看做是一个list；
# 输出t+h+i+s+ +i+s+ +t+e+s+t+2
print('+'.join(test_str2)) # 神奇的是，各类语言对同一种类型的变量的方法命名相似，但是使用方法却截然不同

"""
    六、字符串的驻留机制
        1. 当字符串中仅包涵下划线、字母和数字的时候，会启用字符串的驻留机制（这个范围可能会更大）；
        2. 驻留机制即保存一份相同的不变的字符串，当给不同的变量赋值的时候，变量均指向这个相同的字符串；
"""
m = '1223#'
n = '1223#'
print(id(m), id(n))
# 可以发现两者的id是相同的；

"""
    七、常用的判断相同的方法
        1. == 判断两个变量是否相同，针对字符串则表示二者是否有相同的字符；
        2. is 判断两个对象是否相同，也就是判断是否是同一个地址；[] == []是成立的；
        3. in 判断一个变量是否含有另一个变量，在字符串中则标识一个字符串是否含有另一个字符串；
"""

print('this is a test' == 'this is a test')
print([] == [])

"""
    八、字符串常用的函数
"""
# 1. find，查找字符串中是否含有指定字符；有则返回字符位置，无则返回-1
str = '这是一个字符串'
print(str.find('一个'))
print(str.find('1'))

# 2. index，检测字符串中是否包涵指定字符，有则返回开始位置的的索引，没有则直接报错；
print(str.index('一个'))

# 3. count，检测字符串中某个字段出现的次数
print(str.count('一', 1, 5)) #可以加入索引值

# 4. replace(str1, str2, count)，将字符串的str1字符串内容替换为str2字符串，count表示替换几次，不给值的话则代表全替换
str = '挖呀挖呀挖'
print(str.replace('挖', '123'))

# 5. split，分割字段，返回字符串数组，当不传入内容的时候，则认为是按照空格拆分
print('123   12'.split())

# 6. startwith和endwith，标识字符串是否以。。。开始或结尾
print('123'.startswith('1'))

# 7. lower和upper，将字符串内容转换成大写或者小写
print('aDcadfF'.upper())

# 8. strip、lstrip、rstrip，去除字符串两边的空格
str = ' 1231231 '
print(str.strip()) 

# 9. join，在字符串中间插入某个字符，长用于数组上
print('++'.join(['1','2','3','4']))

# 10. isalpha、isdigit，判断字符串是否完全是字母或者数字
print('123123'.isdigit())

"""
    九、字符串中需要注意的地方
        1. 字符串的本质是字符串序列，和c#一样，是引用类型，有不可变性和驻留性；
        2. Python不支持单字符，即char类型，单字符也是被看做单个字符的字符串；
"""
