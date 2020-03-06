"""

题目一：在O(1)的时间内删除链表结点

给定单向链表的头指针和一个节点指针，定义一个函数在O(1)的时间内删除该结点。

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __del__(self):
        self.val = None
        self.next = None


class Solution:
    def DeleteNode(self, pHead, pNode):
        """"
            需要分类讨论删除的结点是什么结点，链表长度有多少
            如果链表只有一个节点，则删除头结点和指针结点，也相当于 删除的就是尾结点
            如果链表由多个节点，则判断删除的是不是中间结点和头结点，如果是的话O(1)
            如果删除的尾结点，则从头开始删除

        """
        # 判断无效输入
        if not pHead or not pNode:
            return []

        if pNode.next:
            pNext = pNode.next
            pNode.val = pNext.val
            pNode.next = pNext.next
            pNext.__del__()

        elif pNode == pHead:
            pNode.__del__()
            pHead.__del__()
        else:
            Node = pHead
            while Node.next != pNode:
                Node = Node.next
            Node.next = None
            pNode.__del__()

        return pHead


