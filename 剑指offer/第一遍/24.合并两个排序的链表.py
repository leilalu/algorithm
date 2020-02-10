"""
题目描述

输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def Merge(self, pHead1, pHead2):
        """
            需要看出这是一个递归过程：每次都比较两个链表的头结点，将两个链表中值较小的头结点连接到已合并的链表之后

            【注意】 当其中一个链表为空（输入就是空，或者已经合并完毕为空），要返回另一链表
                    当两个链表都为空时，返回另一个链表也是返回空
                    
        :param pHead1:
        :param pHead2:
        :return:
        """
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1

        if pHead1.val < pHead2.val:
            pMergedHead = pHead1
            pMergedHead.next = self.Merge(pHead1.next, pHead2)
        else:
            pMergedHead = pHead2
            pMergedHead.next = self.Merge(pHead1, pHead2.next)

        return pMergedHead




