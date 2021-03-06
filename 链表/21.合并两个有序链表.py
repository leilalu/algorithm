"""
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        # 递归出口
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val < l2.val:
            MergeHead = l1
            MergeHead.next = self.mergeTwoLists(l1.next, l2)
        else:
            MergeHead = l2
            MergeHead.next = self.mergeTwoLists(l1, l2.next)

        return MergeHead