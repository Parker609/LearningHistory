"""
学了数据结构，这个文件主要实现一下里边的各种排序算法，分别是：
1. 冒泡排序
2. 选择排序
3. 插入排序
4. 希尔排序
5. 堆排序
6. 归并排序
7. 快速排序
"""

"""
首先实现冒泡排序，这个应该是所有人接触到的第一种简单排序方法。
原理简单，话不多说，直接上代码。
次代码是最简单的冒泡排序，其实还是有优化的空间，这边暂时不考虑。
"""


def bubble_sort(unsorted_list):
    for i in range(len(unsorted_list)):
        for j in range(i + 1, len(unsorted_list))[::-1]:
            if unsorted_list[j] < unsorted_list[j - 1]:
                temp = unsorted_list[j]
                unsorted_list[j] = unsorted_list[j - 1]
                unsorted_list[j - 1] = temp
    return unsorted_list


"""
选择排序其实也很简单，简单来说，就是在序列中找到最小的元素，并与第一个元素交换。
然后继续从第二个位置开始，以此类推。
复杂度其实还是比较高的。
"""


def select_sort(unsorted_list):
    for i in range(len(unsorted_list)):
        min_index = i
        min_value = unsorted_list[i:][0]
        for j in range(i, len(unsorted_list)):
            if unsorted_list[j] < min_value:
                min_value = unsorted_list[j]
                min_index = j
        unsorted_list[min_index] = unsorted_list[i]
        unsorted_list[i] = min_value
    return unsorted_list


"""
插入排序，原理也并不难理解，扫描整个序列，找到不没按照升序排列的地方的第一个值，把它插到应该在的地方。
直接上代码。
直接插入排序，在于记录数比较少，或者基本有序的情况下，运行速度是非常快的。
"""


def insert_sort(unsorted_list):
    for i in range(len(unsorted_list) - 1):
        flag = 0
        if unsorted_list[i] > unsorted_list[i + 1]:
            temp = unsorted_list.pop(i + 1)
            for i in range(len(unsorted_list)):
                if temp < unsorted_list[i]:
                    flag = 1
                    unsorted_list.insert(i, temp)
                    break
            if flag == 0:
                unsorted_list.append(temp)
    return unsorted_list


"""
希尔排序，稍微有点复杂，这个有点像是插入排序的进化。
思想就是将整个数组分不同的跨度分别进行排序。
之前所有排序的时间复杂度都是O(n2)，这边的希尔排序的复杂度是O(nlogn)，算是降维了。
"""


def shell_sort(unsorted_list):
    gap = 3
    while gap != 1:
        gap = int(gap / 3) + 1
        for i in range(gap):
            for i in range(i, len(unsorted_list) - gap, gap):
                flag = 0
                if unsorted_list[i] > unsorted_list[i + gap]:
                    temp = unsorted_list.pop(i + gap)
                    for i in range(len(unsorted_list)):
                        if temp < unsorted_list[i]:
                            flag = 1
                            unsorted_list.insert(i, temp)
                            break
                    if flag == 0:
                        unsorted_list.append(temp)
    return unsorted_list


"""
堆排序就有些复杂了，首先要构建大顶堆或者小顶堆，用这个堆来确定整个数组的最大最小值。
其中比较复杂的步骤主要有两个，第一，把一个完全二叉树调整为一个大顶堆或者小顶堆；第二，将首位和末尾交换。主要是第一步。
此算法的时间复杂度也是O(nlogn)。
程序看起来确实有点复杂，但是因为每次堆化调整之后的头尾互换之后的序列，里边有很多顺序也是满足堆的，所以并部需要很大的改动。
"""


# 首先，先定义将完全二叉树调整为大顶堆。
# i代表着父节点的编号。
def adjust_heap(unadjusted_heap, i):
    # 对于堆而言，里边的节点编号从1开始，所以可以在未排序的数列前边添加空位，随便加个数就行，反正用不到。
    adjust_point = i
    left_child_index = i*2
    right_child_index = i*2+1
    size = len(unadjusted_heap)
    if right_child_index < size and unadjusted_heap[adjust_point]<unadjusted_heap[right_child_index]:
        adjust_point = right_child_index
    if left_child_index < size and unadjusted_heap[adjust_point] < unadjusted_heap[left_child_index]:
        adjust_point = left_child_index
    if adjust_point != i:
        unadjusted_heap[i], unadjusted_heap[adjust_point] = unadjusted_heap[adjust_point], unadjusted_heap[i]
        adjust_heap(unadjusted_heap,adjust_point)
    return unadjusted_heap

def get_heap(unsorted_list):
    final_node_index = int(len(unsorted_list)/2)
    for i in range(1,final_node_index+1)[::-1]:
        adjust_heap(unsorted_list,i)
    return unsorted_list

def heap_sort(unsorted_list):
    final_leaf_index = int(len(unsorted_list))
    for i in range(3,final_leaf_index+1)[::-1]:
        unsorted_list[:i] = get_heap(unsorted_list[:i])
        unsorted_list[1],unsorted_list[i-1] = unsorted_list[i-1],unsorted_list[1]
    return unsorted_list


"""
快速排序，算是冒泡排序的升级版，其原理简单来说就是给作为基准点的值找到合适的位置。
这边涉及到递归，果然递归是神才会用的东西，贼烦。。。
"""

def quick_sort(unsorted_list,start,end):
    # 因为涉及到递归，先要写一些递归的返回条件。当且仅当序列里只剩下一个元素的时候，下一次的递归显然start >= end，此时递归就可以结束了。
    if start >= end:
        return 0
    # temp存储的是基准点的值。
    temp = unsorted_list[start]
    low = start
    high = end
    while high != low:
        # print(high,low)
        while unsorted_list[high] > temp and high != low:
            high -= 1
        unsorted_list[low] = unsorted_list[high]
        while unsorted_list[low] < temp and high != low:
            low += 1
        unsorted_list[high] = unsorted_list[low]
        # else:
        #     high -= 1
        # if unsorted_list[low] > temp:
        #     unsorted_list[high] = unsorted_list[low]
        # else:
        #     low += 1
    unsorted_list[high] = temp
    quick_sort(unsorted_list,0,low)
    quick_sort(unsorted_list,low+1,end)
    return unsorted_list

"""
这边再讨论说一下归并排序，其实就是分治再合并的过程。
将整个数组分为细小的子数组，再重新合并就可以了。
"""

# 这只是个工具函数，为了之后的操作方便。
def x(x):
    return [x]


# 将两个有序数组合并为一个有序数组。
def merge(list_1,list_2):
    list_3 = []
    while list_1 != [] or list_2!= []:
        if list_1 == [] and list_2 != []:
            list_3.extend(list_2)
            return list_3
        if list_1 != [] and list_2 == []:
            list_3.extend(list_1)
            return list_3
        if list_1[0] < list_2[0]:
            temp = list_1.pop(0)
            list_3.append(temp)
        else:
            temp = list_2.pop(0)
            list_3.append(temp)
    return list_3


# 可以认为一个数列是一个完全二叉树的所有叶子节点。
def merge_sort(unsorted_list):
    new_list = []
    new_list.extend(unsorted_list)
    new_list.extend(unsorted_list)
    new_list = list(map(x,new_list))
    final_node_index = int((len(new_list)-1)/2)
    for i in range(1,final_node_index+1)[::-1]:
        new_list[i] = merge(new_list[i*2],new_list[i*2+1])
    unsorted_list = new_list[1]
    return unsorted_list

if __name__ == '__main__':
    unsorted_list = [5,0, 3, 2, 7, 1, 6, 4, 9, 8]
    # new_list = bubble_sort(unsorted_list)
    # new_list = select_sort(unsorted_list)
    # new_list = insert_sort(unsorted_list)
    # new_list = shell_sort(unsorted_list)
    # new_list = heap_sort(unsorted_list)
    # new_list = quick_sort(unsorted_list,0,9)
    new_list = merge_sort(unsorted_list)
    print(new_list)
