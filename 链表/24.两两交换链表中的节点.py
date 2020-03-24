"""
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        if not head:
            return None

        pre = ListNode(0)
        pre.next = head # 0 1 2 3 4 5
        pNode = head
        preNode = pre

        while pNode:
            pNext = pNode.next
            if not pNext:
                break
            preNode.next = pNext
            pNode.next = pNext.next  # 3->5
            pNext.next = pNode  # 4 -> 3

            preNode = pNode  # 3
            pNode = pNode.next  # 5

        return pre.next


