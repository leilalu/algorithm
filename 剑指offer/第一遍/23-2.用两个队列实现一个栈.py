"""

题目描述

用两个队列来实现一个栈，完成队列的Push和Pop操作。 队列中的元素为int类型。

"""


class Solution:
    def __init__(self):
        self.deque1 = []
        self.deque2 = []

    def push(self, node):
        if len(self.deque1) == 0 and len(self.deque2) == 0:
            self.deque1.append(node)
        if len(self.deque1) > 0 and len(self.deque2) == 0:
            self.deque1.append(node)
        if len(self.deque2) > 0 and len(self.deque1) == 0:
            self.deque2.append(node)

    def pop(self):
        if len(self.deque1) == 0 and len(self.deque2) == 0:
            return

        if len(self.deque1) > 0 and len(self.deque2) == 0:
            while len(self.deque1) > 1:
                self.deque2.append(self.deque1.pop(0))
            return self.deque1.pop(0)

        if len(self.deque2) > 0 and len(self.deque1) == 0:
            while len(self.deque2) > 1:
                self.deque1.append(self.deque2.pop(0))
            return self.deque1.pop(0)




