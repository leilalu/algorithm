"""
题目描述
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。

保证base和exponent不同时为0

"""


class Solution1:
    def Power(self, base, exponent):
        """"
        base = 0 exp = 0 0
        base = 0 exp > 0 0
        base = 0 exp < 0 倒数无意义
        base > 0 exp > 0 累乘
        base > 0 exp < 0 累乘 取倒数
        base > 0 exp = 0 1
        base < 0 exp > 0 累乘
        base < 0 exp < 0 累乘 取倒数
        base < 0 exp = 0 1

        """

        if base == 0.0 and exponent >= 0:
            return 0
        if base == 0.0 and exponent < 0:
            return -1

        power = 1.0
        for i in range(1, abs(exponent)+1):
            power *= base

        if exponent < 0:
            power = 1.0 / power

        return power


class Solution2:
    def Power(self, base, exponent):
        if base == 0.0 and exponent < 0:
            return -1
        if base == 0.0 and exponent >= 0:
            return 0

        power = 1.0
        power = self.PowerCore(base, abs(exponent))

        if exponent < 0:
            power = 1.0 / power

        return power

    def PowerCore(self, base, exponent):
        if exponent == 0:
            return 1
        if exponent == 1:
            return base

        power = 1
        power = self.PowerCore(base, exponent >> 1)
        power *= power

        if exponent & 1 == 1:
            power *= base

        return power



