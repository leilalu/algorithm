"""
题目描述

输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。

"""


class Solution1:
    def NumberOf1(self, n):
        """
        本题考察进制转化，原码和补码，可以分为两步：
                                        第一步写出整数对应的二进制表示；
                                        第二步写出二进制表示中1的个数

        注意到每个非零整数n和n-1进行按位【与】运算，整数n的二进制数中最右边的1就会变成0，那么二进制数中的1的个数就会减少一个，
        因此可以利用一个循环，使得 n = n&(n-1) ，计算经过几次运算减少到0，就是有几个1。

        注意：书中给了另外两种方法，分别是原始n左移一位和右移一位的方法，因为Python不会出现整数溢出的情况，这里就不再考虑这两种方法。

        扩展：判断一个数值是不是2得整数次方，如果是的话，这个数的二进制数中有且只有一个1，那么这个数n会有 n&(n-1) == 0。
             或者求两个整数m和n需要改变m二进制中的多少位才能得到n，可以先做 m^n 的异或运算，然后求这个数中有多少个1。

        :param n:
        :return:
        """

        count = 0
        # 注意 负数要转换为补码
        if n < 0:
            n = n & 0xffffffff
        while n:
            count += 1  # 只要能进循环，至少有一位为1
            n = n & (n-1)
        return count


class Solution2:
    def NumberOf1(self, n):
        """
        利用python的bin函数求二进制

        bin函数将整数转化为二进制，并且是str类型

        :param n:
        :return:
        """

        if n < 0:
            s = bin(n & 0xffffffff)
        else:
            s = bin(n)
        return s.count('1')


if __name__ == '__main__':
    n = 12
    s = Solution1()
    res = s.NumberOf1(n)
    print(res)
