"""
题目描述

输入一个单向链表，输出该链表中倒数第k个结点。

为了符合大多数人的习惯，本题从1开始计数，即链表的尾结点是倒数第1个结点

例如，一个链表有6个结点，从头结点开始，它们的值依次是1、2、3、4、5、6。
这个链表的倒数第3个结点是值为4的结点。

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1:

    def FindKthToRail(self, head, k):
        """
            最简单的思路：倒数第k个结点，就是正数【n-k+1】个结点
            【遍历两遍链表】，第一遍遍历对链表结点🧮，得到链表的结点数n
                                    第二遍遍历 找到第 【n-k+1】 个结点，即为倒数第k个结点

        :param head:
        :param k:
        :return:
        """
        # 检查无效输入
        if not head or k <= 0:
            return

        pNode = head
        count = 0
        while pNode:
            count += 1
            pNode = pNode.next

        pNode = head
        if count < k:
            # k大于链表长度，无意义
            return
        else:
            for i in range(1, count-k+1):
                pNode = pNode.next
            return pNode.val


class Solution2:
    def FindKthToRail(self, head, k):
        """
            【只遍历一次】就能找到倒数第k个结点的方法:【两指针】
            定义两个指针，第一个指针先走k-1步，第二个指针保持不动
                        从第k步开始，第二个指针也从头开始移动，两个指针的距离始终保持k-1
                        当第一个指针走到尾结点时，第二个指针刚好走到倒数第k个结点

            【注意】需要注意，讨论k的取值：1）k <= 0 时无意义
                                       2）k > 链表长度时无意义
                                       3）0 < k <= 链表长度时

        :param head:
        :param k:
        :return:

        """
        if not head or k <= 0:
            return

        # 第一个指针先走k-1步
        first = head
        for i in range(k-1):
            if first.next:
                first = first.next
            else:
                # k大于链表长度
                return None

        # 两个指针同时移动
        second = head
        while first.next:
            first = first.next
            second = second.next

        return second.val


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

    s = Solution2()
    res = s.FindKthToRail(node1, 3)
    print(res)