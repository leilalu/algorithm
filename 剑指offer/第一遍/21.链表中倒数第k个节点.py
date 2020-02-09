"""
题目描述
输入一个链表，输出该链表中倒数第k个结点。

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        if not head or k == 0:
            return None
        pAhead = head

        for i in range(k-1):
            if pAhead.next:
                pAhead = pAhead.next
            else:
                return None

        pBehind = head
        while pAhead.next:
            pAhead = pAhead.next
            pBehind = pBehind.next

        return pBehind