class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
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