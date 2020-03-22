"""
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

说明：不允许修改给定的链表。

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head):
        meetingNode = self.MeetingNode(head)

        if not meetingNode:
            return None

        pNode = meetingNode
        count = 1
        while pNode.next != meetingNode:
            count += 1
            pNode = pNode.next

        first = second = head
        for i in range(count):
            first = first.next

        while first != second:
            first = first.next
            second = second.next

        return first

    def MeetingNode(self, head):
        if not head:
            return None

        slow = head.next
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
