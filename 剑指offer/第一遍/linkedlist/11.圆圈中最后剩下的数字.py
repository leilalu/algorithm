"""
题目描述

0,1,...,n-1 这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字，求出这个圆圈里剩下的最后一个数字


"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1:
    def LastRemaining_Solution(self, n, m):
        """
            这是经典的【约瑟夫环】问题，解决该问题的经典解法是【用环形链表模拟圆圈】

        :param n:
        :param m:
        :return:
        """
        # 检查输入合法
        if n < 1 or m < 1:
            return -1

        # 创建环形链表
        pHead = ListNode(0)
        pNode = pHead
        for i in range(1, n):
            node = ListNode(i)
            pNode.next = node
            pNode = pNode.next
        pNode.next = pHead

        # 删除第m个数字
        while pNode.next != pNode:
            for i in range(1, m):
                # 删除第m个数字，要走m-1步
                pNode = pNode.next
            pNode.next = pNode.next.next

        return pNode.val


class Solution2:
    def LastRemaining_Solution(self, n, m):
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


if __name__ == '__main__':
    n = 5
    m = 3
    s = Solution2()
    res = s.LastRemaining_Solution(n, m)
    print(res)






