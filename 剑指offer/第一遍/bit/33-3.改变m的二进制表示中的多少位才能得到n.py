"""
题目描述

输入两个整数m和n，计算需要改变m的二进制表示中的多少位才能得到n。
比如，10的二进制表示为1010，13的二进制表示为1101，需要改变1010中的3位才能得到1101。

"""


class Solution:
    def Change(self, m, n):
        """
        可以分为两步进行：
            第一步：求两个数的异或
            第二步：统计异或结果中1的位数

        """
        # 第一步：求异或
        s = m ^ n
        # 第二步：计算二进制表示中1的个数
        count = 0
        while s:
            count += 1
            s = s & (s-1)
        return count


if __name__ == '__main__':
    m = 10
    n = 13
    s = Solution()
    res = s.Change(m, n)
    print(res)