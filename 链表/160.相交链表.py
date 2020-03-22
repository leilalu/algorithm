"""
编写一个程序，找到两个单链表相交的起始节点。

注意：

如果两个链表没有交点，返回 null.
在返回结果后，两个链表仍须保持原有的结构。
可假定整个链表结构中没有循环。
程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1:
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None

        stackA = []
        stackB = []

        pNodeA = headA
        pNodeB = headB

        while pNodeA:
            stackA.append(pNodeA)
            pNodeA = pNodeA.next

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
                break

        return res


class Solution2:
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
        if diff > 0:
            for i in range(countA - countB):
                pNodeA = pNodeA.next
        else:
            for i in range(countB - countA):
                pNodeB = pNodeB.next

        while pNodeA != pNodeB:
            pNodeA = pNodeA.next
            pNodeB = pNodeB.next

        return pNodeA














