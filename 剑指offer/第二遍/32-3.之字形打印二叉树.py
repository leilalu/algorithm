"""
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

 

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
  [20,9],
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
        level = []

        stack1 = [root]
        stack2 = []

        while stack1 or stack2:
            if stack1:
                while stack1:
                    node = stack1.pop()
                    level.append(node.val)

                    if node.left:
                        stack2.append(node.left)
                    if node.right:
                        stack2.append(node.right)

                result.append(level)
                level = []

            if stack2:
                while stack2:
                    node = stack2.pop()
                    level.append(node.val)

                    if node.right:
                        stack1.append(node.right)
                    if node.left:
                        stack1.append(node.left)

                result.append(level)
                level = []

        return result