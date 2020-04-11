"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(self, l1: ListNode, l2: ListNode):
    # 首先，初始化链表，先拿到head指针。
    head_start = ListNode(0)
    head = head_start
    carry = 0
    # 当l1和l2均没有下一个值的时候，循环结束。
    while (l1 or l2):
        # 二者不一定是等长的，所以需要先将二者的不等长这个情况考虑进去。
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        if x + y + head.val >= 10:
            carry = 1
        else:
            carry = 0
        head.val = (head.val + (x + y)) % 10
        if l1 != None:
            l1 = l1.next
        if l2 != None:
            l2 = l2.next
        if l1 != None or l2 != None:
            head.next = ListNode(carry)
            head = head.next
    if carry == 1:
        head.next = ListNode(carry)

    return head_start


# 这是针对两个列表而言的，但是如果是两个链表，就比较麻烦了，这涉及到链表的操作。
def two_sum(list_1, list_2):
    res_list = []
    carry = 0
    for n1, n2 in zip(list_1, list_2):
        print(n1, n2)
        # carry 用来表示进位，直接逆序计算。
        res_list.append((n1 + n2) % 10 + carry)
        if (n1 + n2) >= 10:
            carry += 1
        else:
            carry = 0
    if carry == 1:
        res_list.append(carry)
    return res_list


if __name__ == '__main__':
    list_1 = [3, 4, 2]
    list_2 = [4, 6, 5]
    res_list = two_sum(list_1, list_2)
    print(res_list)
