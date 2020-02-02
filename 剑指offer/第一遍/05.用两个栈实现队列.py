"""
题目描述
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

"""


class Solution:
    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def push(self, node):
        self.stack_1.append(node)

    def pop(self):
        """
            【注意】pop前需要检查栈是否为空，这里两个栈都有pop操作，都需要判断

        """
        # 两个栈均为空
        if len(self.stack_1) == 0 and len(self.stack_2) == 0:
            return
        # stack1为空 stack2不空
        elif len(self.stack_2) == 0:
            while len(self.stack_1) > 0:
                self.stack_2.append(self.stack_1.pop())
        return self.stack_2.pop()

