"""
题目描述

用一条语句判断一个整数是不是2的整数次方。

"""


class Solution:
    def isIntegerPowerOf2(self, number):
        if number & (number - 1) == 0:
            return True
        return False


if __name__ == '__main__':
    number = 1
    s = Solution()
    res = s.isIntegerPowerOf2(number)
    print(res)
