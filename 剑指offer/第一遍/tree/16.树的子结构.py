"""
题目描述

输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        """
            分为两步：
                第一步：在树A中找到和树B的根结点的值一样的结点R
                第二步：判断树A中以R为根结点的子树是不是包含和树B一样的结构

        :param pRoot1:
        :param pRoot2:
        :return:
        """

        if not pRoot1 or not pRoot2:
            return False

        result = False
        # 判断根结点
        if pRoot1.val == pRoot2.val:
            result = self.HashSubTreeCore(pRoot1, pRoot2)
        # 判断左子树
        if not result and pRoot1.left:
            result = self.HashSubTreeCore(pRoot1.left, pRoot2)
        # 判断右子树
        if not result and pRoot1.right:
            result = self.HashSubTreeCore(pRoot1.right, pRoot2)

        return result

    def HashSubTreeCore(self, pRoot1, pRoot2):
        # 子树已经完全比对完毕
        if not pRoot2:
            return True
        # 原树已经没有了
        if not pRoot1:
            return False
        # 匹配失败
        if pRoot1.val != pRoot2.val:
            return False
        # 查看左右子树
        return self.HashSubTreeCore(pRoot1.left, pRoot2.left) and self.HashSubTreeCore(pRoot1.right, pRoot2.right)



