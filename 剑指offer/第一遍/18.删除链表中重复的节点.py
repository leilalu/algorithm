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
            return
        pPreNode = None
        pNode = pHead
        while pNode:
            pNext = pNode.next
            needDelete = False
            if pNext and pNext.val == pNode.val:
                needDelete = True
            if not needDelete:
                pPreNode = pNode
                pNode = pNode.next
            else:
                value = pNode.val
                pToBeDeleted = pNode
                while pToBeDeleted and pToBeDeleted.val == value:
                    pNext = pToBeDeleted.next

                    pToBeDeleted.__del__()

                    pToBeDeleted = pNext

                if not pPreNode:
                    pHead = pNext
                else:
                    pPreNode.next = pNext
                pNode = pNext