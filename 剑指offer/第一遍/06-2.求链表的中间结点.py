"""
题目描述

求链表的中间结点。
如果链表中的结点总数为奇数，则返回中间结点；如果结点总数是偶数，则返回中间两个结点的任意一个。

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindMidNode(self, head):
        """
            可以使用【两个指针】，两个指针同时出发，第一个一次走两步，第二个一次走一步。当第一个指针走到链表末尾时，第二个指针刚好在链表中间

            考虑几种特殊情况：
                    1、链表为空
                    2、链表只有1个结点 （属于奇数）

        :param head:
        :return:
        """
        if not head:
            return None

        first = second = head

        # 第一个指针到尾，或到倒数第二个时结束
        while first.next:
            next = first.next
            if next.next:
                second = second.next
                first = next.next
            else:
                break

        return second


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

    s = Solution()
    res = s.FindMidNode(node1)
    print(res.val)