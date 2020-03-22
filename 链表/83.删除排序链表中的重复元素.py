"""
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:

输入: 1->1->2
输出: 1->2
示例 2:

输入: 1->1->2->3->3
输出: 1->2->3

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return None

        pre = ListNode(0)
        pre.next = head
        pNode = head
        preNode = pre

        while pNode:
            if pNode.next and pNode.next.val == pNode.val:
                while pNode.next and pNode.next.val == pNode.val:
                    pNode = pNode.next
                preNode.next = pNode
                
            preNode = preNode.next
            pNode = pNode.next

        return pre.next

