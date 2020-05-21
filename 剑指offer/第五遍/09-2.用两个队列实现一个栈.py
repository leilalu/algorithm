"""
题目：

用两个队列实现一个栈.

"""
from collections import deque


class Solution:
    def __init__(self):
        self.data = deque()
        self.help_data = deque()

    def push(self, x):
        self.data.append(x)

    def pop(self):
        while len(self.data) > 1:
            self.help_data.append(self.data.popleft())

        res = self.data.popleft()
        self.data, self.help_data = self.help_data, self.data

        return res

    def top(self):
        if len(self.data) > 0:
            return self.data[-1]

    def empty(self):
        return len(self.data) == 0
