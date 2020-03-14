"""
请实现 copyRandomList 函数，复制一个复杂链表。
在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，
还有一个 random 指针指向链表中的任意节点或者 null。

"""


class Node:
    def __init__(self, x):
        self.val = int(x)
        self.next = None
        self.random = None


class Solution:
    def copyRandomList(self, head):
        if not head:
            return None

        self.insertCopy(head)
        self.setRandom(head)
        return self.splitList(head)

    def insertCopy(self, head):
        pNode = head
        while pNode:
            pCopy = Node(pNode.val)
            pNext = pNode.next

            pCopy.next = pNext
            pNode.next = pCopy

            pNode = pNext

        return head

    def setRandom(self, head):
        pNode = head
        while pNode:
            pCopy = pNode.next
            if pNode.random:
                pCopy.random = pNode.random.next

            pNode = pCopy.next

        return head

    def splitList(self, head):
        pNode1 = head
        pClone = pNode2 = pNode1.next
        pNode1.next = pNode2.next
        pNode1 = pNode1.next

        while pNode1:
            pNode2.next = pNode1.next
            pNode2 = pNode2.next

            pNode1.next = pNode2.next
            pNode1 = pNode1.next

        return pClone


