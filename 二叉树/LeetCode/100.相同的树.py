"""
给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1:

输入:       1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

输出: true

示例 2:

输入:      1          1
          /           \
         2             2

        [1,2],     [1,null,2]

输出: false

示例 3:

输入:       1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

输出: false

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def isSameTree(self, p, q):
        """"
            递归法

            时间复杂度： O(N) N为树的结点个数，因为每个节点都会访问一次
            空间复杂度：最优情况（完全平衡二叉树）时为 O(logN)，最坏情况下（完全不平衡二叉树）时为 O(N)，用于维护递归栈

        """
        if not p and not q:
            return True

        if type(p) != type(q):
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


class Solution2:
    def isSameTree(self, p, q):
        """"
            迭代法，使用队列代替层次遍历
            复杂度与递归相同
        """
        from collections import deque

        def check(p, q):
            # 如果二者都为空，则返回True
            if not p and not q:
                return True
            # 如果一者为空
            if not p or not q:
                return False
            # 如果值不想等
            if p.val != q.val:
                return False

            return True

        queue = deque([(p, q), ])

        while queue:
            p, q = queue.popleft()
            if not check(q, p):
                return False

            # 注意！！！！！！当p、q都不为空时，才能够添加子结点入队
            if p:
                queue.append((p.left, q.left))
                queue.append((p.right, q.right))

        return True




