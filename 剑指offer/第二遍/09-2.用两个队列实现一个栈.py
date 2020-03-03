"""
题目：

用两个队列实现一个栈.

"""


class Solution:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, node):
        if len(self.queue1) == 0 and len(self.queue2) == 0:
            self.queue1.append(node)
        if len(self.queue1) > 0 and len(self.queue2) == 0:
            self.queue1.append(node)
        if len(self.queue2) > 0 and len(self.queue1) == 0:
            self.queue2.append(node)

    def pop(self):
        node = None
        if len(self.queue1) > 0:
            while self.queue1:
                self.queue2.append(self.queue1.pop(0))
            return self.queue2.pop(0)
        if len(self.queue2) > 0:
            while self.queue2:
                self.queue1.append(self.queue2.pop(0))
            return self.queue1.pop(0)

        return node

