"""
输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root):
        return self.isBalancedCore(root) != -1

    def isBalancedCore(self, root):
        if not root:
            return 0

        left = self.isBalancedCore(root.left)
        if left == -1:
            return -1
        right = self.isBalancedCore(root.right)
        if right == -1:
            return -1

        diff = left - right
        if -1 <= diff <= 1:
            if left > right:
                return left + 1
            else:
                return right + 1
        else:
            return -1


