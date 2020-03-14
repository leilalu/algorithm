"""
输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。
从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。

"""


class Solution:
    def pathSum(self, root, sum):

        if not root:
            return []
        result = []
        stack = [(root, [root.val])]
        self.sums = sum
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right and self.getSum(path) == self.sums:
                result.append(path)

            if node.right:
                stack.append((node.right, path + [node.right.val]))
            if node.left:
                stack.append((node.left, path + [node.left.val]))

        return result

    def getSum(self, path):
        result = 0
        for i in range(len(path)):
            result += path[i]
        return result

