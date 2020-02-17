"""
题目描述

输入一个链表，反转链表后，输出新链表的表头。

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1:
    def ReverseList(self, pHead):
        """
            看到【反转】要想到【从尾到头】要想到使用栈。

            可以顺序遍历链表，将每个结点保存在栈中，然后依次弹栈，返回最后一个结点，就是反转链表的头结点

            时间复杂度是O(n)
            空间复杂度是O(n)

        :param pHead:
        :return:
        """
        # 检查无效输入
        if not pHead:
            return

        # 如果链表只有一个节点
        if not pHead.next:
            return pHead

        # 链表有多个结点
        stack = []
        pNode = pHead
        while pNode:
            stack.append(pNode.val)
            pNode = pNode.next

        # 注意存储的一定要是结点的值，如果储存结点，将会保留结点的指针，最后一个弹出栈的结点的指针一定要变为None
        head = ListNode(stack.pop())
        pNode = head
        while stack:
            node = ListNode(stack.pop())
            pNode.next = node
            pNode = pNode.next
        return self.printLinkedList(head)

    def printLinkedList(self, pHead):
        if not pHead:
            return []
        res = []
        pNode = pHead
        while pNode:
            res.append(pNode.val)
            pNode = pNode.next
        return res


class Solution2:
    def ReverseList(self, pHead):
        """
            不使用辅助空间，直接改变链表的指针方向，使当前结点的下一个结点为上一个节点，但是直接修改指针的话会导致链表断裂，
            因此需要在改变指针方向之前先将后一个结点保存起来

            需要考虑 链表为空或链表中只有一个节点的情况
            【注意】一定要在表头前加一个结点，作为反转链表的尾结点，否则反转链表没有尾结点

        :param pHead:
        :return:
        """
        # 检查无效输入
        if not pHead:
            return

        preNode = None  # 必须手动添加尾结点
        pNode = pHead
        while pNode:
            # 保存起来原来的next
            pNext = pNode.next
            if pNext:
                pNode.next = preNode
                preNode = pNode
                pNode = pNext
            else:
                # 到尾结点
                pNode.next = preNode
                break

        return self.printLinkedList(pNode)

    def printLinkedList(self, pHead):
        if not pHead:
            return []
        res = []
        pNode = pHead
        while pNode:
            res.append(pNode.val)
            pNode = pNode.next
        return res


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6

    s = Solution1()
    res = s.ReverseList(node1)
    print(res)






