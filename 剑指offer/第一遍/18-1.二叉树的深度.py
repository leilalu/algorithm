"""
题目一：二叉树的深度

输入一棵二叉树的根结点，求该树的深度。
从根结点到叶结点一次经过的结点（含根、叶结点）形成的一条路径，最长路径的长度为树的深度

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def TreeDepth(self, pRoot):
        """
            这是在间接考察遍历一棵树



        :param pRoot:
        :return:
        """


class Solution2:
    def TreeDepth(self, pRoot):
        """
            递归法更加简洁
            从另外一个角度理解树的深度，不要一味纠结面试官给出的深度的定义

            如果一棵树只有一个结点， 那么它的深度为1 （左子树深度等于右子树深度）
            如果一棵树只有左子树没有右子树，那么它的深度为其左子树深度+1   （左子树深度 大于 右子树深度）
            如果一棵树只有右子树没有左子树，那么它的深度为其右子树深度+1  （右子树深度 大于 左子树深度）
            如果一棵树既有右子树又有左子树，那么它的深度为左、右子树深度的较大值+1

        :param pRoot:
        :return:
        """
        depth = 0

        if not pRoot:
            return depth

        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)

        if left > right:
            depth = left + 1
        else:
            depth = right + 1

        return depth