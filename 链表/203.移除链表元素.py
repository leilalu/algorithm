"""
删除链表中等于给定值 val 的所有节点。

示例:

输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head, val):
        pre = ListNode(0)
        pre.next = head

        pNode = head
        preNode = pre
        while pNode:
            if pNode.val == val:
                while pNode and pNode.val == val:
                    pNode = pNode.next
                preNode.next = pNode
                if not pNode:
                    break
            pNode = pNode.next
            preNode = preNode.next

        return pre.next


