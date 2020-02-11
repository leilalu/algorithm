"""
题目描述
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向。

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Convert(self, pRootOfTree):

        if not pRootOfTree:
            return None
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree

        # 处理左子树
        self.Convert(pRootOfTree.left)
        left = pRootOfTree.left

        # 把左子树最大的结点与根结点连接在一起
        if left:
            while left.right:
                left = left.right
            pRootOfTree.left = left
            left.right = pRootOfTree

        # 处理右子树
        self.Convert(pRootOfTree.right)
        right = pRootOfTree.right

        # 把右子树最大的结点与根结点连接在一起
        if right:
            while right.left:
                right = right.left

            pRootOfTree.right = right
            right.left = pRootOfTree

        while pRootOfTree.left:
            pRootOfTree = pRootOfTree.left

        return pRootOfTree





