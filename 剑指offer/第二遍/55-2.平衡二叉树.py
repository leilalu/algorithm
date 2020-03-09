"""
输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。

 

示例 1:

给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:

给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def isBalanced(self, root):
        if not root:
            return True

        left = self.getDepth(root.left)
        right = self.getDepth(root.right)

        diff = left - right
        if diff > 1 or diff < -1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)

    def getDepth(self, root):
        depth = 0

        if not root:
            return depth

        left = self.getDepth(root.left)
        right = self.getDepth(root.right)

        if left > right:
            depth = left + 1
        else:
            depth = right + 1

        return depth


class Solution2:
    def isBalanced(self, root):
        return self.depth(root) != -1

    def depth(self, root):
        if not root:
            return 0
        # 后序遍历序列，先左后右
        left = self.depth(root.left)
        if left == -1:
            return -1  # 发现子树不平衡就不必要循环了

        right = self.depth(root.right)
        if right == -1:
            return -1

        diff = left - right

        if diff < -1 or diff > 1:
            # 不平衡
            return -1
        else:
            # 若平衡，返回该子树的深度
            if left > right:
                return 1 + left
            else:
                return 1 + right


