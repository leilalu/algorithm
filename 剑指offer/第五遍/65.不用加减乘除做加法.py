"""
写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。
 
示例:

输入: a = 1, b = 1
输出: 2
 

提示：

a, b 均可能是负数或 0
结果不会溢出 32 位整数

"""


class Solution:
    def add(self, a, b):
        while b != 0:  # 进位不为0
            temp = a ^ b
            b = (a & b) << 1
            a = temp & 0xFFFFFFFF  # 若是负数，则将其变为正数，最终结果要减去4294967296

        return a if a >> 31 == 0 else a - 4294967296


if __name__ == '__main__':
    a = 1
    b = 1
    res = Solution().add(a, b)
    print(res)
