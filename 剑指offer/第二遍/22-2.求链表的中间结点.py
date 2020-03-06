"""
题目描述

求链表的中间结点。

如果链表中的结点总数为奇数，则返回中间结点；如果结点总数是偶数，则返回中间两个结点的任意一个。

"""


class Solution:
    def FindMiddleNode(self, head):
        if not head:
            return None

        first = second = head
        while first.next:
            # 有下一个
            next = first.next
            if next.next:  # 有下下个
                first = next.next
                second = second.next
            else:
                # 有下一个，没下下个
                break
        return next
