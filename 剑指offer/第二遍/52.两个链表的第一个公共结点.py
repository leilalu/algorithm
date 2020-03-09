"""
输入两个链表，找出它们的第一个公共节点。

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1:
    def getIntersectionNode(self, headA, headB):
        """"
            用两个栈来辅助 时间复杂度是O(n)，空间复杂度是O(n)
        """
        if not headA or not headB:
            return None

        stackA = []
        stackB = []

        pNodeA = headA
        while pNodeA:
            stackA.append(pNodeA)
            pNodeA = pNodeA.next

        pNodeB = headB
        while pNodeB:
            stackB.append(pNodeB)
            pNodeB = pNodeB.next

        res = None
        while len(stackA) > 0 and len(stackB) > 0:
            nodeA = stackA.pop()
            nodeB = stackB.pop()
            if nodeA == nodeB:
                res = nodeA
            else:
                return res

        return res


class Solution2:
    def getIntersectionNode(self, headA, headB):
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
            for j in range(-diff):
                pNodeB = pNodeB.next

        while pNodeA and pNodeB:
            if pNodeA != pNodeB:
                pNodeA = pNodeA.next
                pNodeB = pNodeB.next
            else:
                return pNodeA

        return None
