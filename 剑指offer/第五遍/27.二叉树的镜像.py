"""
请完成一个函数，输入一个二叉树，该函数输出它的镜像。

例如输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
镜像输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1

 

示例 1：

输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mirrorTree(self, root):
        # 首先判断输入是否合法
        if not root:
            return None

        # 递归出口是到达叶子结点，叶子结点的镜像是叶子节点本身
        if not root.left and not root.right:
            return root

        left = root.left
        if left:
            left = self.mirrorTree(root.left)

        right = root.right
        if right:
            right = self.mirrorTree(root.right)

        root.left = right
        root.right = left

        return root


