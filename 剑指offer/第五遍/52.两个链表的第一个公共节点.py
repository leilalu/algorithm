"""
输入两个链表，找出它们的第一个公共节点
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None

        countA = 0
        pNodeA = headA
        while pNodeA:
            countA += 1
            pNodeA = pNodeA.next

        countB = 0
        pNodeB = headB
        while pNodeB:
            countB += 1
            pNodeB = pNodeB.next

        diff = countA - countB
        pNodeA = headA
        pNodeB = headB
        if diff > 0:  # A比B长
            for i in range(diff):
                pNodeA = pNodeA.next
        else:
            for i in range(-diff):
                pNodeB = pNodeB.next

        while pNodeA != pNodeB:
            pNodeA = pNodeA.next
            pNodeB = pNodeB.next

        return pNodeA


class Solution1:
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None

        stackA = []
        pNodeA = headA
        while pNodeA:
            stackA.append(pNodeA)
            pNodeA = pNodeA.next

        stackB = []
        pNodeB = headB
        while pNodeB:
            stackB.append(pNodeB)
            pNodeB = pNodeB.next

        res = None
        while stackA and stackB:
            nodeA = stackA.pop()
            nodeB = stackB.pop()
            if nodeA == nodeB:
                res = nodeA
            else:
                return res

        return res


