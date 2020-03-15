"""
题目描述

给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。

"""


class Solution:
    def EntryNodeOfLoop(self, pHead):
        meetingNode = self.Meeting(pHead)

        if not meetingNode:
            return None

        count = 1
        pNode = meetingNode
        while pNode.next != meetingNode:
            count += 1
            pNode = pNode.next

        first = second = pHead
        for i in range(count):
            first = first.next

        while first != second:
            first = first.next
            second = second.next

        return first

    def Meeting(self, pHead):
        if not pHead:
            return None

        slow = pHead.next
        if not slow:
            return None

        fast = slow.next
        while fast and slow:
            if fast == slow:
                return fast

            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
        return None