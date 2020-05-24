"""
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。
假设压入栈的所有数字【均不相等】。
例如，序列 {1,2,3,4,5} 是某栈的压栈序列，序列 {4,5,3,2,1} 是该压栈序列对应的一个弹出序列，但 {4,3,5,1,2} 就不可能是该压栈序列的弹出序列。

示例 1：

输入：pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
输出：true
解释：我们可以按以下顺序执行：
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
示例 2：

输入：pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
输出：false
解释：1 不能在 2 之前弹出。

"""


class Solution:
    def validateStackSequences(self, pushed, popped):
        # 首先判断输入是否合法
        if not pushed and not popped:
            return True

        if not pushed or not popped:
            return False

        if len(pushed) != len(popped) or set(pushed) != set(popped):
            return False

        # 根据压栈序列模拟压栈
        stack = []
        while popped:
            if stack and stack[-1] == popped[0]:
                stack.pop()
                popped.pop(0)
            elif pushed:
                stack.append(pushed.pop(0))

            else:
                return False

        return True

