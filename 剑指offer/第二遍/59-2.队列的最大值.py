"""
请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。

若队列为空，pop_front 和 max_value 需要返回 -1

示例 1：

输入:
["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]

[[],[1],[2],[],[],[]]

输出: [null,null,null,2,1,2]


示例 2：

输入:
["MaxQueue","pop_front","max_value"]

[[],[],[]]

输出: [null,-1,-1]

"""


class MaxQueue:
    def __init__(self):
        from collections import deque
        self.que = deque()  # 原始队列
        self.sort_que = deque()  # 辅助队列

    def max_value(self):
        """"
            返回当前队列中最大的值
        """
        return self.sort_que[0] if self.sort_que else -1

    def push_back(self, value):
        """
            向队列中添加元素，要保持辅助队列排序
        """
        # 原始队列简单加入即可
        self.que.append(value)

        # 辅助队列要将队列中比待入队元素小的都出队
        while self.sort_que and self.sort_que[-1] < value:
            self.sort_que.pop()
        self.sort_que.append(value)

    def pop_front(self):
        """
            元素出队，要判断出队的是不是辅助队列的头，也就是最大的元素，如果是，辅助队列头部也出队
        """
        # 出队一定要判断队列是否为空
        if not self.que:
            return -1
        
        res = self.que.popleft()
        if res == self.sort_que[0]:
            self.sort_que.popleft()
        return res
