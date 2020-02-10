"""
题目描述
输入一个链表，输出该链表中倒数第k个结点。

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def FindKthToRail_1(self, head, k):
        """
            最简单的思路：遍历两遍链表，第一遍遍历对链表结点🧮，得到链表的结点数n
                                    第二遍遍历 找到第 【n-k+1】 个结点，即为倒数第k个结点
        :param head:
        :param k:
        :return:
        """
        if not head or k <= 0:
            return

        pNode = head
        count = 0
        while pNode:
            count += 1

        for i in range(1, count-k+1):
            pNode = pNode.next

        return pNode

    def FindKthToTail_2(self, head, k):
        """
            只遍历一次就能找到倒数第k个结点的方法:【两指针】
            定义两个指针，第一个指针先走k-1步，第二个指针保持不动
                        从第k步开始，第二个指针也从头开始移动，两个指针的距离始终保持k-1
                        当第一个指针走到尾结点时，第二个指针刚好走到倒数dik个结点

            【注意】需要注意，讨论k的取值：1）k <= 0 时无意义
                                       2）k > 链表长度时无意义
                                       3）0 < k <= 链表长度时

        :param head:
        :param k:
        :return:

        """

        if not head or k <= 0:
            return None

        first = head
        for i in range(k-1):
            # 如果k大于链表长度
            if first.next:
                first = first.next
            else:
                return None

        second = head
        while first.next:
            second = second.next
            first = first.next

        return second

        # if not head or k == 0:
        #     return None
        # pAhead = head
        #
        # for i in range(k-1):
        #     if pAhead.next:
        #         pAhead = pAhead.next
        #     else:
        #         return None
        #
        # pBehind = head
        # while pAhead.next:
        #     pAhead = pAhead.next
        #     pBehind = pBehind.next
        #
        # return pBehind