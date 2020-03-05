"""
题目描述
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。

"""


class Solution:
    def NumberOf1(self, n):
        count = 0
        if n < 0:
            n = n & 0xFFFFFFFF
        while n:
            if n & 1:
                count += 1
            n = n >> 1
        return count

    def NumberOf1_2(self, n):
        if n < 0:
            s = bin(n & 0xFFFFFFFF)
        else:
            s = bin(n)

        return s.count('1')

