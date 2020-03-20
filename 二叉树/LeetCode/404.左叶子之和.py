"""
计算给定二叉树的所有左叶子之和。

示例：

    3
   / \
  9  20
    /  \
   15   7

在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0
        self.res = []
        self.sumOfLeftLeavesCore(root)
        return sum(self.res)

    def sumOfLeftLeavesCore(self, root):
        # 判断左子结点
        if root.left:
            # 判断左子结点是不是叶结点
            if not root.left.left and not root.left.right:
                self.res.append(root.left.val)
            else:
                # 如果不是叶结点
                self.sumOfLeftLeaves(root.left)

        if root.right:
            self.sumOfLeftLeaves(root.right)


class Solution2:
    sumValue = 0

    def sumOfLeftLeaves(self, root):
        # 给一个判断是否是左子结点的标记
        self.sumOfLeftLeavesCore(root, False)
        return self.sumValue

    def sumOfLeftLeavesCore(self, root, isLeft):
        if root:
            # 如果该点是左子结点，而且是叶结点
            if isLeft and not root.left and not root.right:
                self.sumValue += root.val

            if root.left:
                self.sumOfLeftLeavesCore(root.left, True)
            if root.right:
                self.sumOfLeftLeavesCore(root.right, False)












