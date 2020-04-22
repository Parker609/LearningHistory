"""
最短路径算法只二，弗洛伊德算法。
也叫做插入值算法，核心思想在于某两个点之间的距离是固定的，如果想要将距离变短，则需要引入第三个点（这边的第三是指其他的某个或者某几个点）
相较于dijkstra算法，此算法代码行数较少，但是时间复杂度是O(n3)。
"""
import numpy as np


def get_path(p_graph,start,end):
    while 1:
        if p_graph[start][end] == end:
            path = [start, end]
            return path
        else:
            mid_path = p_graph[start][end]
            path = get_path(p_graph,start,mid_path)
            path.append(end)
            return path


def floyd(graph,start,end):
    D_len = len(graph)
    p_graph = [[0,1,2,3,4,5]] *6
    p_graph = np.array(p_graph)
    for i in range(D_len):
        for j in range(D_len):
            for k in range(D_len):
                if graph[j][k] == -1 and graph[j][i] != -1 and graph[i][k] != -1:
                    graph[j][k] = graph[j][i] + graph[i][k]
                    p_graph[j][k] = i
                elif graph[j][k] != -1 and graph[j][i] != -1 and graph[i][k] != -1:
                    if graph[j][k] >  graph[j][i] + graph[i][k]:
                        graph[j][k] = graph[j][i] + graph[i][k]
                        p_graph[j][k] = i
    path = get_path(p_graph,start,end)
    return graph[start][end],path

if __name__ == '__main__':
    graph = [[0, 7, 9, -1, -1, 14],
             [7, 0, 10, 15, -1, -1],
             [9, 10, 0, 11, -1, 2],
             [-1, 15, 11, -1, 6, -1],
             [-1, -1, -1, 6, 0, 9],
             [14, -1, 2, -1, 9, 0]]
    g,p = floyd(graph,0,4)

    print(g)
    print(p)