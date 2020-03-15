"""
给定一个二叉树，返回它的 前序 遍历。

 示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,2,3]

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def preorderTraversal(self, root):
        """"
            递归写法

            时间复杂度是：O(n)

            空间复杂度是：O(n)

        """
        if not root:
            return []

        res = []

        def getPreOrder(root):
            if root:
                res.append(root.val)
            if root.left:
                getPreOrder(root.left)
            if root.right:
                getPreOrder(root.right)

        getPreOrder(root)

        return res


class Solution2:
    def preorderTraversal(self, root):
        """"
            迭代写法
        """
        if not root:
            return []

        res = []
        stack = [root]
        while stack:
            cur = stack.pop()
            res.append(cur.val)

            # 注意！由于使用栈，一定要先加右子结点，再加左子结点！
            if cur.right:
                stack.append(cur.right)

            if cur.left:
                stack.append(cur.left)

        return res


