"""
输入一个链表，输出该链表中倒数第k个节点。
为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。
例如，一个链表有6个节点，从头节点开始，它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个节点是值为4的节点。


示例：

给定一个链表: 1->2->3->4->5, 和 k = 2.

返回链表 4->5.

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1:
    def getKthFromEnd(self, head, k):
        if not head:
            return None
        stack = []
        pNode = head
        while pNode:
            stack.append(pNode)
            pNode = pNode.next

        res = None
        if k <= len(stack):
            for i in range(k):
                res = stack.pop()

        return res


class Solution2:
    def getKthFromEnd(self, head, k):
        if not head:
            return None
        first = second = head
        for i in range(k-1):
            first = first.next
            if not first:
                return None

        while first.next:
            first = first.next
            second = second.next

        return second



