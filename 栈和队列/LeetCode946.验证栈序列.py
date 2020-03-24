"""
给定 pushed 和 popped 两个序列，每个序列中的 值都不重复，
只有当它们可能是在最初空栈上进行的推入 push 和弹出 pop 操作序列的结果时，返回 true；否则，返回 false 。

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
        if not pushed or not popped:
            return True

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


if __name__ == '__main__':
    pushed = [1, 2, 3, 4, 5]
    popped = [4, 3, 5, 1, 2]
    res = Solution().validateStackSequences(pushed, popped)
    print(res)
