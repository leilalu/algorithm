"""

题目三：之字形打印二叉树

请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Print(self, pRoot):
        if not pRoot:
            return []

        stack1 = []
        stack2 = []
        res = []
        level = []

        stack1.append(pRoot)
        while stack1 or stack2:
            if stack1:
                while stack1:
                    current = stack1.pop()
                    level.append(current.val)

                    if current.left:
                        stack2.append(current.left)
                    if current.right:
                        stack2.append(current.right)

                res.append(level)
                level = []

            if stack2:
                while stack2:
                    current = stack2.pop()
                    level.append(current.val)

                    if current.right:
                        stack1.append(current.right)
                    if current.left:
                        stack1.append(current.left)

                res.append(level)
                level = []

        return res






