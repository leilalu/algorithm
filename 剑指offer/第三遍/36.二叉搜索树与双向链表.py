"""
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。

"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def treeToDoublyList(self, root):
        if not root:
            return root
        self.tail = self.head = None

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            if not self.head:
                self.head = self.tail = root
            if self.head == root:
                return dfs(root.right)
            self.tail.right = root
            root.left = self.tail
            self.tail = self.tail.right
            dfs(root.right)

        dfs(root)
        self.tail.right = self.head
        self.head.left = self.tail
        return self.head
