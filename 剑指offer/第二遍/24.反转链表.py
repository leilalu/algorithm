"""
题目描述

输入一个链表，【反转】链表后，输出新链表的表头。

"""


class Solution:
    def ReverseList(self, pHead):
        if not pHead:
            return

        preNode = None
        pNode = pHead  # 一定要从第一个节点开始反转，否则第一个节点的next指针将指向第二个节点

        while pNode.next:
            pNext = pNode.next
            pNode.next = preNode
            preNode = pNode
            pNode = pNext

        pNode.next = preNode
        return pNode
