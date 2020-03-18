"""
题目：
给定一棵二叉树和其中的一个节点，如何找【中序遍历】序列的下一个结点？
树中的结点除了有两个分别指向左、右子结点的指针，还有一个指向父结点的指针。

"""


class Solution:
    def FindNextNode(slef, pNode):
        if not pNode:
            return None

        res = None
        if pNode.right:
            right = pNode.right
            while right.left:
                right = right.left
            res = right

        elif pNode.next:
            parent = pNode.next
            current = pNode
            while parent and current == parent.right:
                current = parent
                parent = parent.next
            res = parent

        return res
