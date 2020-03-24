"""
给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例 1:

给定链表 1->2->3->4, 重新排列为 1->4->2->3.
示例 2:

给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reorderList(self, head):
        if not head:
            return None
        Merged_head = merge = ListNode(0)

        slow = fast = head
        while fast.next:
            pNext = fast.next
            if pNext.next:
                slow = slow.next
                fast = pNext.next
            else:
                break

        temp = slow.next
        back = self.reverseList(temp)
        slow.next = None

        i = 1
        while head and back:
            if i & 1 == 1:
                merge.next = head
                merge = merge.next
                head = head.next
            else:
                merge.next = back
                merge = merge.next
                back = back.next
            i += 1

        if head:
            merge.next = head
        if back:
            merge.next = back

        return Merged_head.next

    def reverseList(self, head):
        if not head:
            return None
        preNode = None
        pNode = head
        while pNode:
            pNext = pNode.next
            pNode.next = preNode
            preNode = pNode
            pNode = pNext

        return preNode

