"""
题目描述
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，【重复的结点不保留】，返回链表头指针。
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        """"
            删除重复的结点，那么头结点也可能被删除，因此需要在头结点前加上一个结点

        """
        if not pHead:
            return
        pre = ListNode(0)
        pre.next = pHead
        pNode = pHead
        preNode = pre

        while pNode:
            if pNode.next and pNode.val == pNode.next.val:
                while pNode.next and pNode.val == pNode.next.val:
                    pNode = pNode.next
                preNode.next = pNode.next
                pNode = pNode.next

            else:
                preNode = preNode.next
                pNode = pNode.next

        return pre.next