"""
题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

"""


class Solution:
    def jumpFloorII(self, number):
        """
            用数学归纳法可以证明
                    f(n) = 2 ^ (n-1)

            实现循环代替递归

        :param number:
        :return:
        """
        res = 1
        if number >= 2:
            for i in range(number-1):
                res = res * 2
        return res