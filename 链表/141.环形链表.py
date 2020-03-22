"""

给定一个链表，判断链表中是否有环。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
如果 pos 是 -1，则在该链表中没有环。

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head):
        if not head:
            return False
        slow = head.next
        if not slow:
            return False

        fast = slow.next
        while fast and slow:
            if fast == slow:
                return True
            slow = slow.next
            fast = fast.next

            if fast:
                fast = fast.next

        return False


