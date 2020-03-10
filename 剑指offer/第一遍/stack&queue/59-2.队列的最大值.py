"""
题目二：队列的最大值

请定义一个队列并实现函数max得到队列里的最大值，要求函数max、push_back和pop_front的时间复杂度都是O(1)

"""


class MaxQueue:
    def __init__(self):
        # python内置的deque的popleft 时间复杂度才是O(1)，python数组的pop(0)的时间复杂度是O(n)
        from collections import deque
        self.data = deque()  # 原始队列
        self.max_data = deque()  # 辅助队列

    def max_value(self):
        return self.max_data[0] if self.max_data else -1

    def push_back(self, value):
        self.data.append(value)

        while self.max_data and value > self.max_data[-1]:
            self.max_data.pop()
        self.max_data.append(value)

    def pop_front(self):
        if not self.data:
            return -1

        res = self.data.popleft()
        if res == self.max_data[0]:
            self.max_data.popleft()
        return res

