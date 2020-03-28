"""
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

示例1：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            mergeHead = l1
            mergeHead.next = self.mergeTwoLists(l1.next, l2)
        else:
            mergeHead = l2
            mergeHead.next = self.mergeTwoLists(l1, l2.next)

        return mergeHead
