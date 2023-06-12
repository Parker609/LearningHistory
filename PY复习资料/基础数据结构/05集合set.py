"""
    Set是集合，一般是用于对List的处理，适用场景：
        1. 去重：把一个列表变成集合，则自动去重，相当于js里的set；
        2. 关系测试：测试两组数据之间的交集、并集和差集等关系；
"""

"""
    一、集合的特性：
        1. 集合使用set表示，也可以使用{}表示，与字典不同，字典在{}中存储键值对，set存储单值；
        2. 注意：x={}表示的是字典，x=set()是表示空集合；
        3. 集合中不存在重复元素，会自动过滤；
        4. 集合中的元素是无序的；
        5. 集合中的元素是可hash的，可hash的意义是在生命周期中，该元素的保持不变的；如string和tuple
        6. 集合的最底层其实就是用字典的key来实现的，比方说：{1,2,3}其实是{'1': None, '2': None, '3': None}
"""

print({1, 2, 3, 3})
print(set([1,2,3,1,2,3,3,3,3]))
print(len(set([1,2,3,1,2,3,3,3,3])))

"""
    二、集合中提供的方法
        1. add()，向集合中添加元素
        2. remove()，删除集合中的指定元素，如果元素不存在则报错
        3. discard()，删除指定元素，如果元素不存在，不进行任何操作
        4. pop()，删除并返回集合中的元素，但是集合是无序的，所以这个操作不常用
        5. clear()，删除整个集合中所有的元素；
        6. copy()，集合的复制；
        7. difference()，两个集合的差集，产生新的集合
        8. difference_update()，集合差集，但是不返回值，只是改变当前集合，最好别用；
        9. intersection()，集合的交集
        10. intersection_update()，交集，改变当前集合
        11. union()，并集
        12. update()，并集，改变当前集合
        13. symmetric_difference()，两个集合的对称差集，即a集合中有，b中有，但不共有的；
        14. symmetric_difference_update()，对称差集，改变当前集合
        15. isdisjoint()，判断交集是否为空
        16. issubset()，是否为子集
        17. issuperset()，是否为父集（超集）
"""
temp_set = {1, 2, 3, 4}
target_set = {1, 2, 3, 5}

print(temp_set)

# 添加元素
temp_set.add(12)
print(temp_set)

# 删除元素
temp_set.discard(12)
print(temp_set)

# 清空集合
temp_set.clear()
print(temp_set)

# 7. 集合相互比较：差集，a中有，b中没有的值
temp_set = {1, 2, 3, 7}
print(temp_set.difference(target_set))

# 9. 集合的交集：两个集合中都有的值
print(temp_set.intersection(target_set))

# 10. 集合的并集：两个集合合并再去重
print(temp_set.union(target_set))

# 11. 集合的对称差集
print(temp_set.symmetric_difference(target_set))

# 判断是否是子集
print({1, 2, 3}.issubset({1, 2, 3, 5}))

# 判断两者是否没有交集
print({1, 2, 3}.isdisjoint({5, 4, 3}))

# 判断是否是超集
print({1, 2, 3}.issuperset({2, 3}))

"""
    三、集合的运算
        1. 判断某个元素是否在集合中，in
        2. & 返回交集，相当于intersection
        3. | 返回元素的并集，相当于union
        4. - 返回差集，相当于difference
        5. ^ 返回对称差集
        6. == 集合是否值相等
        7. > 超集
        8. < 子集
"""


# 7. 集合相互比较：差集，a中有，b中没有的值
temp_set = {1, 2, 3, 7}
print(temp_set - target_set)

# 9. 集合的交集：两个集合中都有的值
print(temp_set & target_set)

# 10. 集合的并集：两个集合合并再去重
print(temp_set | target_set)

# 11. 集合的对称差集
print(temp_set ^ target_set)

# 判断是否是子集
print({1, 2, 3} < {1, 2, 3, 5})

# 判断两者是否有交集
print({1, 2, 3} == {5, 4, 3})

# 判断是否是超集
print({1, 2, 3} > {2, 3})

# 数组去重
t = list({i for i in [1,2,3,4,4,4,5,5,5,7]})
print(t)