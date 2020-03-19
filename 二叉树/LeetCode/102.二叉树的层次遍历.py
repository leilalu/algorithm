"""

给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root):
        """"
            二叉树的层次遍历，注意使用队列，以及记录每一行的结点数
        """
        if not root:
            return []

        queue = [root]
        level = []
        curLevel = 1
        nextLevel = 0
        res = []

        while queue:
            node = queue.pop(0)
            level.append(node.val)
            curLevel -= 1

            if node.left:
                queue.append(node.left)
                nextLevel += 1
            if node.right:
                queue.append(node.right)
                nextLevel += 1

            if curLevel == 0:
                res.append(level)
                level = []
                curLevel = nextLevel
                nextLevel = 0

        return res



