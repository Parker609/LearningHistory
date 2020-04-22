"""
找出数组中重复的数字。
在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

来源：力扣（LeetCode）
"""

# 使用哈希表来存，用个字典来装。
def get_repeat_num(unsorted_list):
    temp_dic = {}
    for i in unsorted_list:
        if i not in temp_dic:
            temp_dic[i] =1
        else:
            return i

if __name__ == '__main__':
    unsorted_list = [2, 3, 1, 0, 2, 5, 3]
    res = get_repeat_num(unsorted_list)
    print(res)