"""
请实现 copyRandomList 函数，复制一个复杂链表。
在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。

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
        self.copyNode(head)
        self.setRandom(head)
        return self.splitList(head)

    def copyNode(self, head):
        pNode = head
        while pNode:
            copy = Node(pNode.val)
            pNext = pNode.next
            pNode.next = copy
            copy.next = pNext
            pNode = pNext

    def setRandom(self, head):
        pNode = head

        while pNode:
            pCopy = pNode.next
            if pNode.random:
                pCopy.random = pNode.random.next
            pNode = pCopy.next

    def splitList(self, head):
        pNode = head
        pClone = pCopy = pNode.next
        pNode.next = pCopy.next
        pNode = pNode.next

        while pNode:
            pCopy.next = pNode.next
            pCopy = pCopy.next
            pNode.next = pCopy.next
            pNode = pNode.next

        return pClone




