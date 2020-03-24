"""
设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) -- 将元素 x 推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。
示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.

"""


class MinStack:

    def __init__(self):
        self.data = []
        self.min_data = []

    def push(self, x: int) -> None:
        self.data.append(x)
        if not self.min_data or self.min_data[-1] > x:
            self.min_data.append(x)
        else:
            self.min_data.append(self.min_data[-1])

    def pop(self) -> None:
        if self.data and self.min_data:
            self.min_data.pop()
            return self.data.pop()

    def top(self) -> int:
        if self.data:
            return self.data[-1]

    def getMin(self) -> int:
        if self.min_data:
            return self.min_data[-1]