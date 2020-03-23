"""
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

示例 1:

输入: 1->2->3->3->4->4->5
输出: 1->2->5
示例 2:

输入: 1->1->1->2->3
输出: 2->3
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return None

        preNode = pre = ListNode(0)
        pre.next = head
        pNode = head
        while pNode:
            # 注意 要判断的是pNode.next是否存在
            if pNode.next and pNode.val == pNode.next.val:
                while pNode.next and pNode.val == pNode.next.val:
                    pNode = pNode.next
                preNode.next = pNode.next
                pNode = pNode.next
            else:
                pNode = pNode.next
                preNode = preNode.next
        return pre.next
