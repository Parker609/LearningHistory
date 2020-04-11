"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""


# 最简单的办法就是暴力破解，先写一个。
def lengthOfLongestSubstring(s: str):
    str_list = list(s)
    res_list = []
    for i in range(len(str_list)):
        temp_list = []
        temp_list.append(str_list[i])
        for j in range(i + 1, len(str_list)):
            if str_list[j] not in temp_list:
                temp_list.append(str_list[j])
            else:
                break
        if len(temp_list) > len(res_list):
            res_list = temp_list
    return len(res_list)


# 经过思考之后，发现这个问题可以简化，可以使用双指针游走的办法，只循环一次就可以得出结果。这边需要注意，首指针可能出现回退的情况，所以在更改首指针的时候，它目前所在的位置。
def lengthOfLongestSubstring_02(s):
    max_dis = 0
    start_point = 0
    end_point = 0
    s_list = list(s)
    hash_map = {}
    emu_list = enumerate(s_list)
    for index, word in emu_list:
        if word in hash_map:
            dis = end_point - start_point
            if dis > max_dis:
                max_dis = dis
            if start_point <= hash_map[word]:
                start_point = hash_map[word] + 1
        hash_map[word] = index
        end_point += 1
    dis = end_point - start_point
    if dis > max_dis:
        max_dis = dis
    return max_dis


if __name__ == '__main__':
    s = lengthOfLongestSubstring_02("")
    print(s)
