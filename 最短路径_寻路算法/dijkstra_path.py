"""
最短路径求法只Dijkstra算法，用于求带权值的图的最短路径。
这个思想是基于贪心算法的，也可以算是动态规划法，从前往后规划。
"""


# 起点编号设置为start，终点编号设置为end，则构建代码如下所示。
def dijkstra(graph, start, end):
    cost_init = graph[start]
    # group_1 和 group_2 都是index。
    group_1 = [start]
    group_2 = [i for i in range(len(graph))]
    group_2.remove(start)
    while group_2 != []:
        min_index = -1
        for i in group_2:
            if min_index == -1:
                min_index = i
            else:
                if cost_init != -1 and cost_init[min_index] > cost_init[i]:
                    min_index = i
        group_1.append(min_index)
        group_2.remove(min_index)
        for i in range(len(graph)):
            if cost_init[i] == -1 and cost_init[min_index] != -1 and graph[min_index][i] != -1:
                cost_init[i] = cost_init[min_index] + graph[min_index][i]
            elif cost_init[i] != -1 and cost_init[min_index] != -1 and graph[min_index][i] != -1:
                if cost_init[i] > cost_init[min_index] + graph[min_index][i]:
                    cost_init[i] = cost_init[min_index] + graph[min_index][i]
    return cost_init



if __name__ == '__main__':
    graph = [[0, 7, 9, -1, -1, 14],
             [7, 0, 10, 15, -1, -1],
             [9, 10, 0, 11, -1, 2],
             [-1, 15, 11, -1, 6, -1],
             [-1, -1, -1, 6, 0, 9],
             [14, -1, 2, -1, 9, 0]]
    res = dijkstra(graph, 0, 4)
    print(res)
