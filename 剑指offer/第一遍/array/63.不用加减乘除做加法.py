"""
题目：

写一个函数，求两个整数之和，要求在函数体内不得使用"+"、"-"、"x"、"\" 四则运算符号

"""


class Solution:
    def Add(self, num1, num2):
        while num2 != 0:
            temp = num1 ^ num2
            num2 = (num1 & num2) << 1
            num1 = temp & 0xFFFFFFFF
        return num1 if num1 >> 31 == 0 else num1 - 4294967296

