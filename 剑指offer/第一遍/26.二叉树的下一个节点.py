"""
题目描述

给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。

"""


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None



class Solution:
    def GetNext(self, pNode):
        """
            对给定结点的位置进行分类讨论
                1）当该节点有右子树时，下一个节点就是它的右子树的最左结点
                2）当该节点没有右子树时
                        1）如果该节点是它父结点的左子结点，下一个结点就是它的父结点
                        2）如果该节点是它父结点的右子结点，可以沿着父结点的指针一直向上遍历，直到找到一个是它的父结点的左子结点的结点

        :param pNode:
        :return:
        """

        if not pNode:
            return None
        pNext = None

        if pNode.right:
            # 当该节点有右子树时
            pRight = pNode.right
            while pRight.left:
                pRight = pRight.left

            pNext = pRight

        elif pNode.next:
            pParent = pNode.next
            pCurrent = pNode

            while pParent and pCurrent == pParent.right:
                pCurrent = pParent
                pParent = pParent.next

            pNext = pParent

        return pNext


