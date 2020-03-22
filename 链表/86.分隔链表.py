"""
给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。

你应当保留两个分区中每个节点的初始相对位置。

示例:

输入: head = 1->4->3->2->5->2, x = 3
输出: 1->2->2->4->3->5

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head, x):
        """"
            使用两个链表，分别将小于x和大于等于x的结点链起来
            虽然看着像是创建了两个新链表，但其实没有开辟新的空间

            时间复杂度是O(N)
            空间复杂度是O(1)
        """
        # 分别创建小于x的before链表和大于x的after链表 表头使用哑结点
        before_head = before = ListNode(0)
        after_head = after = ListNode(0)

        # 遍历原链表
        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next

            head = head.next

        # 将两个链表链接起来
        after.next = None
        before.next = after_head.next

        return before_head.next














