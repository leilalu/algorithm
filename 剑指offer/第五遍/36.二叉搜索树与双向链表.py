"""
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。

我们希望将这个二叉搜索树转化为双向循环链表。
链表中的每个节点都有一个前驱和后继指针。对于双向循环链表，第一个节点的前驱是最后一个节点，最后一个节点的后继是第一个节点。

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
        # 先将双向链表链好
        newRoot = self.treeToDoublyListCore(root)
        # 保存头节点
        head = newRoot

        # 找到尾节点
        while newRoot.right:
            newRoot = newRoot.right

        # 首尾链接起来
        head.left = newRoot
        newRoot.right = head

        return head

    def treeToDoublyListCore(self, root):
        if not root:
            return root

        # 递归出口：叶节点
        if not root.left and not root.left:
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
