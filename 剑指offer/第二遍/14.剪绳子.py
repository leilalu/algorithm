"""
题目描述

给你一根长度为n的绳子，请把绳子剪成【整数长】的m段（m、n都是整数，n>1并且m>1），每段绳子的长度记为k[0],k[1],...,k[m]。
请问k[0]xk[1]x...xk[m]可能的最大乘积是多少？

例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

"""


class Solution:
    def cutRope(self, number):
        if number < 2:
            return 0
        if number == 2:
            return 1
        if number == 3:
            return 2

        products = [0] * (number + 1)
        products[0] = 0
        products[1] = 1
        products[2] = 2
        products[3] = 3

        max = 0
        for n in range(4, number+1):
            max = 0
            for i in range(1, n//2 + 1):
                product = products[i] * products[n-i]
                if product > max:
                    max = product
            products[n] = max

        max = products[number]

        return max