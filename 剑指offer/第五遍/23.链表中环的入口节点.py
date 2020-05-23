"""
题目描述

给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。

"""


class Solution:
    def EntryNodeOfLoop(self, pHead):
        meetingNode = self.Meeting(pHead)
        # 如果快慢指针没有相遇，则没有环
        if not meetingNode:
            return None

        # 如果存在环，确定环的长度
        count = 1
        pNode = meetingNode
        while pNode.next != meetingNode:
            pNode = pNode.next
            count += 1

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

        # 用双指针确定链表中是否有环
        slow = pHead.next
        # 如果只有一个节点
        if not slow:
            return None

        fast = slow.next
        while fast and slow:
            # 循环出口
            if fast == slow:
                return fast

            # slow走一步，fast走两步
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next

        return None

