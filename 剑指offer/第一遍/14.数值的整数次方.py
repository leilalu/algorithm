"""
题目描述
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。

保证base和exponent不同时为0

"""


class Solution:
    def Power_1(self, base, exponent):
        res = 1
        if base == 0.0:
            return 0
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        # 重点需要考虑底数为0，指数为负的情况
        if base == 0.0 and exponent < 0:
            return 0
        for i in range(1, abs(exponent)+1):
            res = res * base
        if exponent < 0:
            return 1.0/res
        else:
            return res

    def Power_2(self, base, exponent):
        if base == 0.0 and exponent < 0:
            return 0.0
        if exponent < 0:
            absExponent = -exponent
        else:
            absExponent = exponent

        result = self.PowerWithUnsignedExponent(base, absExponent)

        if exponent < 0:
            return 1.0/result
        else:
            return result

    def PowerWithUnsignedExponent(self, base, exponent):
        if exponent == 0:
            return 1
        if exponent == 1:
            return base

        result = self.PowerWithUnsignedExponent(base, exponent >> 1)
        result *= result
        if exponent & 0x1 == 1:
            result *= base

        return result


if __name__ == '__main__':
    base = 2
    exponent = -3
    s = Solution()
    res = s.Power_2(base, exponent)
    print(res)



