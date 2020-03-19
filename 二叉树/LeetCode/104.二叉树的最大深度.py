"""
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root):
        # 注意！！！！递归出口！！！！ 因此在计算左子树和右子树的深度时，不需要再判断根结点是否为空了，递归是可以完成计算的！
        if not root:
            return 0
        # 判断左子树深度
        left = self.maxDepth(root.left)
        # 判断右子树深度
        right = self.maxDepth(root.right)

        # 计算本结点深度
        if left > right:
            depth = left + 1
        else:
            depth = right + 1

        return depth
