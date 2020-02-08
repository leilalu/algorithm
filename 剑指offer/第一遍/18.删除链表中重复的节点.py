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
            return pHead
        temp = ListNode(0)
        temp.next = pHead
        pre, cur = temp, pHead
        while cur:
            if cur.next and cur.val == cur.next.val:
                while cur.next and cur.next.val == cur.val:
                    cur = cur.next
                pre.next = cur.next
                cur = cur.next
            else:
                pre = pre.next
                cur = cur.next
        return temp.next




