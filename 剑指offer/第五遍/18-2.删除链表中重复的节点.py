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
        # 首先判断输入是否合法
        if not pHead:
            return None

        # 由于删除的可能是头节点，因此需要添加辅助的头指针
        pre = ListNode(0)
        pre.next = pHead
        pNode = pHead
        preNode = pre

        while pNode:
            if pNode.next and pNode.next.val == pNode.val:
                while pNode.next and pNode.next.val == pNode.val:
                    pNode = pNode.next
                preNode.next = pNode.next
                pNode = pNode.next

            else:
                pNode = pNode.next
                preNode = preNode.next

        return pre.next
