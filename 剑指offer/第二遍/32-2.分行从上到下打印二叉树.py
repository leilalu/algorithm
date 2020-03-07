"""
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

 

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
        if not root:
            return []

        result = []
        queue = [root]
        curLevel = 1
        nextLevel = 0

        level = []
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
                result.append(level)
                curLevel = nextLevel
                nextLevel = 0
                level = []

        return result
