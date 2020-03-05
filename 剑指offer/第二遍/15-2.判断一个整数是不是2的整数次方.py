"""
题目描述

用一条语句判断一个整数是不是2的整数次方。

"""


class Solution:
    def IsPowerOf2(self, number):
        return True if number & (number-1) == 0 else False


if __name__ == '__main__':
    number = 1
    res = Solution().IsPowerOf2(number)
    print(res)
