"""
写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。

 

示例:

输入: a = 1, b = 1
输出: 2

"""


class Solution:
    def add(self, a, b):
        while b != 0:  # 直到没有进位 跳出循环
            temp = a ^ b
            b = (a & b) << 1  # 进位
            a = temp & 0xFFFFFFFF   # 异或结果
        return a if a >> 31 == 0 else a - 4294967296



