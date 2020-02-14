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

        result = False

        if pRoot1 and pRoot2:

            if pRoot1.val == pRoot2.val:
                result = self.DoesTree1HaveTree2(pRoot1, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.left, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.right, pRoot2)

        return result

    def DoesTree1HaveTree2(self, pRoot1, pRoot2):

        if not pRoot2:
            return True

        if not pRoot1:
            return False

        if pRoot1.val != pRoot2.val:
            return False

        return self.DoesTree1HaveTree2(pRoot1.left, pRoot2.left) and self.DoesTree1HaveTree2(pRoot1.right, pRoot2.right)


