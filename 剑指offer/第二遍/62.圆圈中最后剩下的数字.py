"""
0,1,,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。

例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。

 

示例 1：

输入: n = 5, m = 3
输出: 3

示例 2：

输入: n = 10, m = 17
输出: 2
 

限制：

1 <= n <= 10^5
1 <= m <= 10^6

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def lastRemaining(self, n, m):
        if n < 1 or m < 1:
            return -1
        # 首先创建环形链表
        pHead = ListNode(0)  # 创建头结点
        pNode = pHead
        for i in range(1, n):
            # 创建新结点
            node = ListNode(i)
            pNode.next = node
            pNode = pNode.next
        # 尾结点与头结点相连
        pNode.next = pHead

        # 删除第m个结点
        while pNode.next != pNode:
            for i in range(m-1):
                pNode = pNode.next
            pNode.next = pNode.next.next
        return pNode.val


if __name__ == '__main__':
    n = 70866
    m = 116922

    s = Solution()
    res = s.lastRemaining(n, m)
    print(res)


