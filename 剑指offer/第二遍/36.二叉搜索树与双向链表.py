"""
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。

"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root):
        if not root:
            return None

        if not root.left and not root.right:
            return root

        if root.left:
            left = root.left
            self.treeToDoublyList(left)
            while left.right:
                left = left.right
            root.left = left
            left.right = root

        if root.right:
            right = root.right
            self.treeToDoublyList(right)
            while right.left:
                right = right.left
            root.right = right
            right.left = root

        while root.left:
            root = root.left

        return root
