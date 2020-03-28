"""
输入两个链表，找出它们的第一个公共节点。

如果两个链表没有交点，返回 null.
在返回结果后，两个链表仍须保持原有的结构。
可假定整个链表结构中没有循环。
程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        pNodeA = headA
        countA = 0
        while pNodeA:
            countA += 1
            pNodeA = pNodeA.next

        pNodeB = headB
        countB = 0
        while pNodeB:
            countB += 1
            pNodeB = pNodeB.next

        diff = countA - countB
        pNodeA = headA
        pNodeB = headB
        if diff > 0:
            for i in range(diff):
                pNodeA = pNodeA.next
        else:
            for i in range(-diff):
                pNodeB = pNodeB.next

        while pNodeA != pNodeB:
            pNodeA = pNodeA.next
            pNodeB = pNodeB.next

        return pNodeA


