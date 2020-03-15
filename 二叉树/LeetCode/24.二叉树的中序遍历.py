"""
给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def inorderTraversal(self, root):
        """"
            递归写法

            时间复杂度：O(n)。递归函数 T(n) = 2 * T(n/2) + 1。

            空间复杂度：最坏情况下需要空间O(n)，平均情况为O(logn)。

        """
        if not root:
            return []

        res = []

        def InOrder(root):
            if root.left:
                InOrder(root.left)
            if root:
                res.append(root.val)
            if root.right:
                InOrder(root.right)

        InOrder(root)

        return res


class Solution2:
    def inorderTraversal(self, root):
        """"
            迭代写法

        """

        if not root:
            return []

        res = []
        stack = []
        cur = root
        while cur or stack:
            # 首先添加所有的左子结点
            while cur:
                stack.append(cur)
                cur = cur.left
            # 左子结点遍历完，
            cur = stack.pop()
            res.append(root.val)
            cur = cur.right

        return res


















