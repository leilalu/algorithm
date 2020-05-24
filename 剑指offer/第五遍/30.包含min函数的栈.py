"""
定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。

"""


class MinStack:

    def __init__(self):
        self.data = []
        self.min_data = []

    def push(self, x: int):
        self.data.append(x)
        if not self.min_data or self.min_data[-1] > x:
            self.min_data.append(x)
        else:
            self.min_data.append(self.min_data[-1])

    def pop(self) -> None:
        if self.data and self.min_data:
            self.data.pop()
            self.min_data.pop()

    def top(self) -> int:
        if self.data:
            return self.data[-1]
        else:
            return -1

    def min(self) -> int:
        if self.min_data:
            return self.min_data[-1]
        else:
            return -1
