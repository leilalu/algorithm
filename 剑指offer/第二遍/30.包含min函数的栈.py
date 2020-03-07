"""
定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。

 

示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.min();   --> 返回 -2.
 

提示：

各函数的调用总次数不超过 20000 次

"""


class MinStack:

    def __init__(self):
        self.stack = []
        self.stack_data = []

    def push(self, x):
        self.stack.append(x)

        if x < self.stack_data[-1] or not self.stack_data:
            self.stack_data.append(x)
        else:
            self.stack_data.append(self.stack_data[-1])

    def pop(self):
        # pop之前一定要先经过判断
        if self.stack and self.stack_data:
            self.stack.pop()
            self.stack_data.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]

    def min(self):
        if self.stack_data:
            return self.stack_data[-1]