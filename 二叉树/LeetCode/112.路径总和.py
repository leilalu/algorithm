"""
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root, sum):
        if not root:
            return False

        res = []
        stack = [(root, [root.val])]

        while stack:
            node, path = stack.pop()
            if not node.left and not node.right and self.getSum(path) == sum:
                res.append(path)
            if node.right:
                stack.append((node.right, path+[node.right.val]))

            if node.left:
                stack.append((node.left, path+[node.left.val]))

        return res

    def getSum(self, path):
        sumValue = 0
        for i in path:
            sumValue += i
        return sumValue

