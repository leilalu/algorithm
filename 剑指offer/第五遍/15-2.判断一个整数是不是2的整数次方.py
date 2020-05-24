"""
题目描述

用一条语句判断一个整数是不是2的整数次方。

"""

""""
如果一个整数是2的整数次方，那么它的二进制表示中，有且只有一位是1，其他都是0

"""


class Solution:
    def IsPowerOf2(self, number):
        return not number & (number-1)
        # return True if number & (number-1) == 0 else False


if __name__ == '__main__':
    number = 2
    res = Solution().IsPowerOf2(number)
    print(res)
