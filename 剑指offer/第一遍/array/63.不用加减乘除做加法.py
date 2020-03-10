"""
题目：

写一个函数，求两个整数之和，要求在函数体内不得使用"+"、"-"、"x"、"\" 四则运算符号

"""


class Solution:
    def Add(self, num1, num2):
        while num2 != 0:  # 直到没有进位了
            # 第一步 各位相加 不进位
            temp = num1 ^ num2
            # 第二步 计算进位
            num2 = (num1 & num2) << 1
            # 第三步 把两者相加（其实就是进行循环），但是要处理一下python的无限长整型
            num1 = temp & 0xFFFFFFFF
        return num1 if num1 >> 31 == 0 else num1 - 4294967296

