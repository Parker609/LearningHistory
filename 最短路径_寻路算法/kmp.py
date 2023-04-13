"""
对于字符串的子字符串匹配问题，有神人提出了KMP算法（看毛片算法，哈哈哈）。
主要是对于子字符串进行分析，并排列了next数据列表，并依照这个表减免不必要的操作。

移动位数 = 已匹配的字符数 - 对应的部分匹配值
"""


# 拿到某个字符串的所有前缀和后缀的值。
def get_fix(string):
    pre_str_list = []
    su_fix_list = []

    pre_str = string[:-1]
    su_fix = string[1:]

    pre_str_len = len(pre_str)
    su_fix_len = len(su_fix)

    for i in range(1, pre_str_len + 1):
        pre_str_list.append(pre_str[:i])

    for i in range(0, su_fix_len):
        su_fix_list.append(su_fix[i:])
    return pre_str_list, su_fix_list


def get_arr_next(string):
    string_len = len(string)
    next_arr = []
    for i in range(1, string_len + 1):
        flag = 1
        pre_fix, su_fix = get_fix(string[:i])
        for i in pre_fix:
            if i in su_fix:
                flag = 0
                next_arr.append(len(i))
                break
        if flag == 1:
            next_arr.append(0)
    return next_arr


# 返回部分匹配值。
def analysis_child_string(parent_string, child_string):
    next_arr = get_arr_next(child_string)
    parent_string_len = len(parent_string)

    i = 0

    while i + len(child_string) <= parent_string_len:
        flag = 0
        for j in range(len(child_string)):
            if parent_string[i+j] != child_string[j]:
                break
            flag += 1
        if flag == 0:
            i += 1
        elif flag == len(child_string):
            return i
        else:
            i += flag - next_arr[flag-1]
    return "未找到"

if __name__ == '__main__':
    string = "BBC ABCDAB ABCDABCDABDE"
    child_string = "ABCDABC"
    res = analysis_child_string(string ,child_string)
    print(res)
