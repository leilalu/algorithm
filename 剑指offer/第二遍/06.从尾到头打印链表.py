"""
题目：
输入一个链表的头结点，【从尾到头】反过来打印每个节点的值

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def ReverseLinkedList1(pHead):
    if not pHead:
        return []
    stack = []
    pNode = pHead
    while pNode:
        stack.append(pNode.val)
        pNode = pNode.next

    res = []
    while stack:
        res.append(stack.pop())

    return res


def ReversedLinkedList2(listNode):
    res = []

    def PrintListNode(listNode):
        if listNode:
            PrintListNode(listNode.next)
            res.append(listNode.val)

    PrintListNode(listNode)

    return res

if __name__ == '__main__':
    listNode = ListNode(1)
    listNode_1 = ListNode(2)
    listNode_2 = ListNode(3)
    listNode_3 = ListNode(4)
    listNode.next = listNode_1
    listNode_1.next = listNode_2
    listNode_2.next = listNode_3

    res = ReversedLinkedList2(listNode)
    print(res)
