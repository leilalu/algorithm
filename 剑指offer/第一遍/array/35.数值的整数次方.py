"""
题目描述
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。

保证base和exponent不同时为0

不得使用库函数，同时不需要考虑大数问题

"""


class Solution1:
    def Power(self, base, exponent):
        """
        本题需要对base 和 exponent进行充分的分类讨论，要考虑到各种特殊值，base和exponent都可以取正数、负数、零三种值：
            1、当base为正数时，expoent为0、正数时，累乘即可
            2、当base为正数，expoent为负数时，先对expoent取绝对值，求累乘后取倒数
            3、当base为负数时，expoent为0、正数时，累乘即可
            4、当base为负数时，expoent为负数时，先对exponent取绝对值，求累乘后取倒数
            5、当base为零时，exponent为0时无意义，expoent为正数时，为0
            6、当base为零时，expoent为负数时将出现分母为0的情况，异常

        总结：
            base可以分为零和其他，exponent可以分为【零、正数】和负数分别讨论

            一个循环，时间复杂度时O(n)

        """
        if base == 0.0 and exponent >= 0:
            return 0

        # 错误处理，分母为倒数时有问题
        if base == 0.0 and exponent < 0:
            return -1


        # 计算累乘
        result = 1.0
        for i in range(1, abs(exponent)+1):
            result *= base
        # 若指数为负，则返回倒数
        if exponent < 0:
            result = 1.0 / result

        return result


class Solution2:
    def Power(self, base, exponent):
        """
        【递归法快速做乘方！】

        根据【a的n次方】的性质，可以找到时间复杂度为 O(logn) 的解法：

            a^n = a^(n/2) * a^(n/2) n为偶数
                = a^((n-1)/2) * a^((n-1)/2) n为奇数

        可以通过递归来求

        Tips：1、可以用右移一位运算带代替除以2 【>> 1】 == 【/2】
              2、可以用位与1 代替求余运算  【 & 0x1】 == 【% 2】 【& 0x1】 == 1则说明最后一位是1，是奇数，否则是偶数

        """

        if base == 0.0 and exponent < 0:
            return -1
        if base == 0.0 and exponent >= 0:
            return 0

        result = 1.0

        result = self.PowerWithUnsignedExponent(base, abs(exponent))

        if exponent < 0:
            result = 1 / result

        return result

    def PowerWithUnsignedExponent(self, base, exponent):
        # 0次方
        if exponent == 0:
            return 1
        # 1次方
        if exponent == 1:
            return base

        # 计算 a ^ (n/2)
        result = self.PowerWithUnsignedExponent(base, exponent >> 1)  # 右移两位相当于除以2
        # 计算 a ^n = a^(n/2) * a^(n/2)
        result *= result

        # 判断指数是奇数还是偶数
        if exponent & 0x1 == 1:  # 位与1相当于进行求余操作 判断最后一位是奇数还是偶数，最后一位是1的话，就是奇数，否则是偶数
            result *= base

        return result


if __name__ == '__main__':
    base = 2
    exponent = -3
    s = Solution2()
    res = s.Power(base, exponent)
    print(res)



