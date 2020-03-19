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

        stack = []
        inorder = []
        while stack or root:
            # 首先遍历所有的左子结点
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            # 开始pop才开始打印结点
            inorder.append(root.val)
            root = root.right

        return inorder

















