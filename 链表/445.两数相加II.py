"""
给定两个非空链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储单个数字。将这两数相加会返回一个新的链表。



你可以假设除了数字 0 之外，这两个数字都不会以零开头。

进阶:

如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。

示例:

输入: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
输出: 7 -> 8 -> 0 -> 7

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """"
            利用栈
        """
        if not l1:
            return l2
        if not l2:
            return l1

        pNode1 = l1
        stack1 = []
        while pNode1:
            stack1.append(pNode1.val)
            pNode1 = pNode1.next

        pNode2 = l2
        stack2 = []
        while pNode2:
            stack2.append(pNode2.val)
            pNode2 = pNode2.next

        circle = 0
        res = pre = ListNode(0)
        while stack1 and stack2:
            num1 = stack1.pop()
            num2 = stack2.pop()
            sumValue = num1 + num2 + circle
            circle = 0
            if sumValue >= 10:
                sumValue -= 10
                circle = 1

            curNode = ListNode(sumValue)
            pre.next = curNode
            pre = pre.next

        while stack1:
            num1 = stack1.pop()
            sumValue = num1 + circle
            circle = 0
            if sumValue >= 10:
                sumValue -= 10
                circle = 1

            curNode = ListNode(sumValue)
            pre.next = curNode
            pre = pre.next

        while stack2:
            num2 = stack2.pop()
            sumValue = num2 + circle
            circle = 0
            if sumValue >= 10:
                sumValue -= 10
                circle = 1

            curNode = ListNode(sumValue)
            pre.next = curNode
            pre = pre.next

        if circle > 0:
            pre.next = ListNode(1)
            pre = pre.next

        # 反转链表
        back = self.reverseList(res.next)

        return back

    def reverseList(self, head):
        if not head:
            return head

        preNode = None
        pNode = head
        while pNode:
            pNext = pNode.next
            pNode.next = preNode
            preNode = pNode
            pNode = pNext

        return preNode






