"""
题目二：删除链表中重复的节点
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __del__(self):
        self.val = None
        self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        """
        由于链表已经排序，因此重复结点是相邻的
        :param pHead:
        :return:
        """

        if not pHead:
            return None

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



