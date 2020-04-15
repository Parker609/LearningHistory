"""
这个py文件是用于解决数据结构中Josephus问题，构建循环链表，并模拟里边的问题，从而最终输出死亡顺序编号。
"""


# 我们使用字典的结构来模拟循环链表。
class Josephus():
    def __init__(self, n):
        self.table,self.table_len = self.table_init(n-1)
        self.death_order = []
        self.counter = 0

    # 初始化循环链表。
    def table_init(self, n):
        table = {}
        for i in range(1, 1 + n):
            table[i] = {"cur": i + 1}
        table[1 + n] = {"cur": 1}
        return table,len(table)

    # 定义在当前的环中，以编号m为起点，第n个人自杀。
    def start_shoot(self, m, n):
        for i in range(n - 2):
            table_m = self.table[m]["cur"]
            m = table_m
        self.death_order.append(self.table[m]["cur"])
        self.table[m]["cur"] = self.table[self.table[m]["cur"]]["cur"]
        self.counter += 1
        return self.table[m]["cur"]

    def circle_shooting(self, m, n):
        while (self.counter < self.table_len):
            m = self.start_shoot(m,n)
        print(self.death_order)



if __name__ == '__main__':
    josephuse = Josephus(41)
    print(josephuse.table)
    josephuse.circle_shooting(1, 3)
