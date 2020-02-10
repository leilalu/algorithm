"""
题目描述
输入一个链表，反转链表后，输出新链表的表头。

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def ReverseList_1(self, pHead):
        """
             使用栈
        :param pHead:
        :return:
        """
        if not pHead:
            return
        if not pHead.next:
            # 只有头结点一个节点
            return pHead

        stack = []
        pNode = pHead
        while pNode:
            stack.append(pNode.val)

        head = ListNode(0)
        pNode = ListNode(stack.pop())
        head.next = pNode
        while stack:
            node = ListNode(stack.pop())
            pNode.next = node
            pNode = pNode.next

        return head.next

    def ReverseList_2(self, pHead):
        """
            不使用辅助空间，直接改变链表的指针方向，使当前结点的下一个结点为上一个节点，但是直接修改指针的话会导致链表断裂，
            因此需要在改变指针方向之前先将后一个结点保存起来

            需要考虑 链表为空或链表中只有一个节点的情况

        :param pHead:
        :return:
        """
        res = None
        pNode = pHead
        pPre = None

        while pNode:
            # 先把下一个节点保存起来
            pNext = pNode.next

            if not pNext:
                # 遍历到尾结点
                res = pNode

            pNode.next = pPre

            pPre = pNode
            pNode = pNext

        return res









