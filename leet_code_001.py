"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""


# 方法1，暴力破解，直接两层循环嵌套，暴力解决，时间复杂度很高，因为是两层循环，所以是Ｏ(N2)。
def twoSum01(list, target):
    for i in range(len(list)):
        for j in range(len(list)):
            if i == j:
                continue
            res = list[i] + list[j]
            if res == target:
                print([i, j])
                exit()
    return None


# 方法2，可以使用哈希表来做，这样十分容易。
# 顺便对哈希表做一个简单解释，即将数据哈希处理，并将结果作为存储单元的index进行存储，对大规模存储数据是十分合用的。
def twoSum02(list, target):
    hash_map = {}
    enu_list = enumerate(list)
    for index,num in enu_list:
        num2 = target - num
        # hash_map是一个字典，在字典中的 in 可以查询 key 是否存在。
        if num2 in hash_map:
            return [hash_map[num2],index]
        hash_map[num] = index
    return None


if __name__ == '__main__':
    nums = [7, 2, 11, 15]
    target = 9
    # twoSum01(nums, target)
    print(twoSum02(nums,target))

