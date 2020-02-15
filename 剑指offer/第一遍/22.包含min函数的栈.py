"""
题目描述

定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数。

在该栈中，调用min、push、pop的时间复杂度都是O(1)

"""


class Solution:
    """
        很自然能够想到，在栈里添加一个成员变量用来记录栈中最小的元素，每压栈一个新元素，就与这个最小的元素进行比较，如果比当前最小的元素还要笑，就更新最小元素
        但是存在问题：如果当前最小的元素弹出栈了，那么如何得到下一个最小的元素呢？

        这就要求我们记录下来每一次压栈时当前的最小元素

        使用一个辅助栈来记录栈最小元素
        每压入栈一个新元素，就比较它和辅助栈栈顶的最小元素，如果新元素更小，则将新元素同时压入栈和辅助栈，如果辅助栈栈顶元素更小，则再次压入
        辅助栈栈顶的元素，作为本次压栈的最小元素
        每弹出栈一个元素，同时弹出数据栈栈顶和辅助栈栈顶

    """
    def __init__(self):
        self.stack = []
        self.stack_min = []

    def push(self, node):

        self.stack.append(node)

        if not self.stack_min or node < self.stack_min[-1]:
            self.stack_min.append(node)
        else:
            self.stack_min.append(self.stack_min[-1])

    def pop(self):

        if self.stack and self.stack_min:
            self.stack.pop()
            self.stack_min.pop()

    def top(self):
        return self.stack[-1]

    def min(self):
        if self.stack and self.stack_min:
            return self.stack_min[-1]
