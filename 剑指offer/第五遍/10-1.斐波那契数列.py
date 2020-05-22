"""
写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项。斐波那契数列的定义如下：

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

"""


class Solution:
    def fib(self, n):
        """"
            从下网上计算，保存中间项。时间复杂度是O(n)
        """
        # 首先判断输入是否合法
        if n < 0:
            return None
        tmp = [0, 1]
        for i in range(2, n+1):
            tmp[i % 2] = tmp[0] + tmp[1]

        return tmp[n % 2] % 1000000007

    def fib1(self, n):
        """"
            递归法，时间复杂度是n的指数次方
        """
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n > 1:
            return self.fib1(n-1) + self.fib1(n-2)

if __name__ == '__main__':
    n = 5
    res = Solution().fib(n)
    print(n)
