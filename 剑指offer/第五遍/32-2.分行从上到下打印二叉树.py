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


class Solution:
    def levelOrder(self, root):
        # 首先判断输入为空的情况
        if not root:
            return []

        res = []
        queue = [root]
        thisLevel = 1
        nextLevel = 0
        level = []

        while queue:
            node = queue.pop(0)
            level.append(node.val)
            thisLevel -= 1

            if node.left:
                queue.append(node.left)
                nextLevel += 1

            if node.right:
                queue.append(node.right)
                nextLevel += 1

            if thisLevel == 0:
                res.append(level)
                level = []
                thisLevel = nextLevel
                nextLevel = 0

        return res

