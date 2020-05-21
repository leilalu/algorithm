"""
题目：
给定一棵二叉树和其中的一个节点，如何找【中序遍历】序列的下一个结点？
树中的结点除了有两个分别指向左、右子结点的指针，还有一个指向父结点的指针。

"""
"""
如果有右子树，返回右子树中的最左节点
如果没有右子树：如果该节点是其父节点的左子结点，则返回父节点
              如果该节点是其父节点的右子节点，则沿着父节点一直向上遍历，直到找到一个是它父节点的左子结点的节点，返回这个节点的父节点

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def FindNextNode(self, pNode):
        # 首先判断输入是否合法
        if not pNode:
            return None
        # 分情况讨论节点的位置

        res = None

        # 如果该节点有右子树，则下一个节点是右子树的最左节点
        if pNode.right:
            right = pNode.right
            while right.left:
                right = right.left
            res = right
        # 如果没有右子树，判断是否有父节点
        elif pNode.next:
            parent = pNode.next
            current = pNode
            # 该节点是父节点的右子结点，则需要一直向上遍历到该节点是父节点的左子结点
            while parent and current == parent.right:
                current = parent
                parent = parent.next
            # 左子结点的下一节点是他的父节点
            res = parent

        return res





