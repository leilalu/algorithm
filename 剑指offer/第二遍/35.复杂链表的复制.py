"""

题目描述
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。
（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）

"""


class Node:
    def __init__(self, x):
        self.val = int(x)
        self.next = None
        self.random = None


class Solution:
    def copyRandomList(self, head):
        if not head:
            return []

        self.InserNode(head)
        self.SetRandom(head)
        return self.SplitLinkedList(head)


    def InserNode(self, head):
        pNode = head
        while pNode:
            copy = Node(pNode.val)
            pNext = pNode.next
            pNode.next = copy
            copy.next = pNext

            pNode = pNext


    def SetRandom(self, head):
        pNode = head

        while pNode:
            pCopy = pNode.next
            if pNode.random:
                pCopy.random = pNode.random.next
            pNode = pCopy.next

    def SplitLinkedList(self, head):
        pNode = head
        pClonedHead = pClonedNode = pNode.next
        pNode.next = pClonedHead.next
        pNode = pNode.next

        while pNode:
            pClonedNode.next = pNode.next
            pClonedNode = pClonedNode.next
            pNode.next = pClonedNode.next
            pNode = pNode.next

        return pClonedHead


