"""
实现函数double Power(double base, int exponent)，求base的exponent次方。不得使用库函数，同时不需要考虑大数问题。

 

示例 1:

输入: 2.00000, 10
输出: 1024.00000
示例 2:

输入: 2.10000, 3
输出: 9.26100
示例 3:

输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25

"""


class Solution1:
    def myPow(self, x, n):
        """"
            循环累乘做乘方，会超时
        """
        if n == 0:
            return 1
        if x == 0:
            if n > 0:
                return 0
            else:
                return float('inf')

        # 乘方
        res = 1
        for i in range(abs(n)):
            res *= x

        if n < 0:
            res = 1.0 / res

        return res


class Solution2:
    def myPow(self, x, n):
        if n == 0:
            return 1

        if x == 0:
            if n > 0:
                return 0
            else:
                return float('inf')

        power = self.PowerCore(x, abs(n))
        if n < 0:
            power = 1.0 / power

        return power

    def PowerCore(self, x, n):
        if n == 0:
            return 1

        if x == 0:
            if n > 0:
                return 0
            else:
                return float('inf')

        power = self.PowerCore(x, n >> 1)
        power *= power

        if n & 1 == 1:
            power *= x

        return power

























    #     if n == 0:
    #         return 1
    #     if x == 0:
    #         if n > 0:
    #             return 0
    #         else:
    #             return float('inf')
    #
    #     power = 1
    #     power = self.PowerCore(x, abs(n))
    #
    #     if n < 0:
    #         power = 1.0 / power
    #
    #     return power
    #
    # def PowerCore(self, x, n):
    #     if n == 0:
    #         return 1
    #     if n == 1:
    #         return x
    #
    #     power = 1
    #     power = self.PowerCore(x, n >> 1)
    #     power *= power
    #     if n & 1 == 1:
    #         power *= x
    #     return power
    #






