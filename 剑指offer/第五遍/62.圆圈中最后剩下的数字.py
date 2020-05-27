"""
0,1,,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。

例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。


示例 1：

输入: n = 5, m = 3
输出: 3
示例 2：

输入: n = 10, m = 17
输出: 2

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def lastRemaining(self, n, m):
        # 首先检查输入是否合法
        if n < 1 or m < 1:
            return -1

        # 首先创建环形链表
        pHead = ListNode(0)
        pNode = pHead
        for i in range(1, n):
            # 创建新节点
            node = ListNode(i)
            # 链接在后面
            pNode.next = node
            pNode = pNode.next
        # 首尾相连
        pNode.next = pHead  # 此时pNode指向尾部

        # 删除第m个节点
        while pNode.next != pNode:   # 循环终止条件是，环形链表中只有一个节点了
            for i in range(m-1):
                pNode = pNode.next
            pNode.next = pNode.next.next

        return pNode.val


class Solution2:
    def lastRemaining(self, n, m):
        """

            思路2：用数学归纳法推导出递推公式，
            设有n个人（编号0~(n-1))，从0开始报数，报到(m-1)的退出，剩下的人继续从0开始报数。令f[i]表示i个人时最后胜利者的编号，则有递推公式：
            f[1]=0;
            f[i]=(f[i-1]+m)%i; (i>1)
            通过递推公式即可求得f[n]。

        :param n:
        :param m:
        :return:
        """
        if n < 1 or m < 1:
            return -1
        last = 0
        for i in range(2, n+1):
            last = (last + m) % i
        return last






