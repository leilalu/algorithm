"""
题目描述

求链表的中间结点。如果链表中的结点总数为奇数，则返回中间结点；如果结点总数是偶数，则返回中间两个结点的任意一个。

"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindMidNode(self, head):
        """
            可以使用【两个指针】，两个指针同时出发，第一个一次走两步，第二个一次走一步。当第一个指针走到链表末尾时，第二个指针刚好在链表中间

        :param head:
        :return:
        """
        if not head:
            return None

        first = head
        second = head
        while first.next:
            first = first.next.next
            second = second.next

        return second