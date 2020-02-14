"""
题目描述
输入两个链表，找出它们的第一个公共结点。

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1:
    def FindFirstCommonNode(self, pHead1, pHead2):
        """
            需要理解题目中的【公共结点】的含义：公共结点不仅是value相等，而且下一个结点也相同，因此在第一个公共结点之后，一直到尾结点，
            两个链表所有的结点都是重合的。

            因此可以发现，如果两个链表有公共结点，那么公共结点一定出现在两个链表的尾部。如果我们从后往前开始比较，
            那么最后一个相同的结点就是我们要找的【第一个公共结点】

            但是在单向链表中，只能从前往后按顺序遍历，不能从后往前遍历。因此最后达到的尾结点却要最先进行比较，这符合"后进先出"，
            因此可以想到使用栈来解决。

            分别将两个链表的结点放入两个栈中，这样两个链表的尾结点就位于两个栈的栈顶，接下来比较两个栈顶的结点是否相同。
            如果相同就弹栈，接着比较下一个栈顶，直到找到最后一个相同的结点。


            时间复杂度O(m+n) 空间复杂度O(m+n)
            用空间换时间

        :param pHead1:
        :param pHead2:
        :return:
        """

        # 检查无效输入
        if not pHead1 or not pHead2:
            return

        stack1 = []
        stack2 = []

        # 第一个链表的栈
        pNode1 = pHead1
        while pNode1:
            stack1.append(pNode1)
            pNode1 = pNode1.next

        # 第二个链表的栈
        pNode2 = pHead2
        while pNode2:
            stack2.append(pNode2)
            pNode2 = pNode2.next

        # 开始弹栈比较大小
        res = None
        while len(stack1) > 0 and len(stack2) > 0:
            p1 = stack1.pop()
            p2 = stack2.pop()
            if p1.val == p2.val:
                res = p1
            else:
                return res
        return res

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
    def FindFirstCommonNode(self, pHead1, pHead2):
        """
            如果不使用辅助栈，可以分析使用栈的原因：我们想同时遍历到达两个栈的尾结点。
            当两个链表的长度不相同时，如果我们从头开始遍历，那么到达尾结点的时间就不一致。

            首先遍历两个链表得到它们的长度，就能知道哪个链表长，哪个链表短，以及长的链表比短的链表多几个节点。
            在第二次遍历的时候，先在长的链表上走若干步，使两个链表未走的长度相同，接着同时在两个链表上遍历，找到的第一个相同的结点就是
            它们的第一个公共结点。

        :param pHead1:
        :param pHead2:
        :return:
        """
        # 检查无效输入
        if not pHead1 or not pHead2:
            return
        # 第一个链表长度
        length1 = 0
        pNode1 = pHead1
        while pNode1:
            length1 += 1
            pNode1 = pNode1.next
        # 第二个链表长度
        length2 = 0
        pNode2 = pHead2
        while pNode2:
            length2 += 1
            pNode2 = pNode2.next

        # 调整两个链表使其未走长度相同
        diff = length1 - length2
        pNode1 = pHead1
        pNode2 = pHead2
        if diff > 0:
            # 第一个链表长
            while diff > 0:
                diff -= 1
                pNode1 = pNode1.next
        else:
            # 第二个链表长
            while diff < 0:
                diff += 1
                pNode2 = pNode2.next

        # 同时遍历两个等长的链表，找第一个相同的结点
        while pNode1 and pNode2:
            if pNode1 == pNode2:
                return pNode1
            else:
                pNode1 = pNode1.next
                pNode2 = pNode2.next

        return None

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
    pHead1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    pHead2 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node7 = ListNode(7)

    pHead1.next = node2
    node2.next = node3
    node3.next = node6
    node6.next = node7

    pHead2.next = node5
    node5.next = node6

    s = Solution2()
    print(s.printLinkedList(pHead1))
    print(s.printLinkedList(pHead2))

    res = s.FindFirstCommonNode(pHead1, pHead2)

    print(res)



