class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def lastNumber(self, n, m):
        if n < 1 or m < 1:
            return -1

        pHead = ListNode(0)
        pNode = pHead
        for i in range(1, n):
            node = ListNode(i)
            pNode.next = node
            pNode = pNode.next
        pNode.next = pHead

        while pNode.next != pNode:
            for i in range(m-1):
                pNode = pNode.next
            pNode.next = pNode.next.next

        return pNode.val

