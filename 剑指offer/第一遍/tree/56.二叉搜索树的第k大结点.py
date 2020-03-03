"""
题目描述

给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）    中，按结点数值大小顺序第三小结点的值为4。

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.treeNode = []

    def inOrder(self, pRoot):
        if len(self.treeNode) < 0:
            return None
        # 左子树
        if pRoot.left:
            self.inOrder(pRoot.left)
        # 根结点
        self.treeNode.append(pRoot)
        # 右子树
        if pRoot.right:
            self.inOrder(pRoot.right)

    def KthNode(self, pRoot, k):
        if not pRoot or k == 0:
            return None

        # 计算二叉树的中序遍历序列
        self.inOrder(pRoot)

        # 如果k比二叉树的结点数都大，则返回None
        if len(self.treeNode) < k:
            return None

        return self.treeNode[k-1]

