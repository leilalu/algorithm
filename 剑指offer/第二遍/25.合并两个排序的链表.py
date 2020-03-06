"""
题目描述
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。

"""


class Solution:
    def Merge(self, pHead1, pHead2):
        if not pHead1:
            return pHead2

        if not pHead2:
            return pHead1

        if pHead1.val < pHead2.val:
            mergeHead = pHead1
            mergeHead.next = self.Merge(pHead1.next, pHead2)
        else:
            mergeHead = pHead2
            mergeHead.next = self.Merge(pHead1, pHead2.next)

        return mergeHead