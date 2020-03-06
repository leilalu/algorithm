"""
题目描述
输入一个链表，输出该链表中倒数第k个结点。

"""


class Solution:
    def FindKthToTail(self, head, k):
        if not head or not k <= 0:
            return None

        first = second = head

        for i in range(k-1):
            if first.next:
                first = first.next
            else:
                return None

        while first.next:
            first = first.next
            second = second.next
        return second