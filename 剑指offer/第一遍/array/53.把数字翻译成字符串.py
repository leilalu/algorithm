"""
题目描述

给定一个数字，我们按照如下规则把它翻译成字符串：
0翻译成'a'，1翻译成'b'……11翻译成'1'，……25翻译成'z'。
一个数字可能有多个翻译。例如：12258有5种不同的翻译，分别是'bccfi'、'bwfi'、'bczi'、'mcfi'和'mzi'
请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

"""


class Solution:
    def GetTranslationCount(self, number):
        """"
            定义函数f(i)表示从第i位数字开始的不同翻译数目，题目最后会返回f(0)

            f(i) = f(i+1) + g(i, i+1) * f(i+2)
            g(i, i+1) 当第i位和dii+1位数字拼接起来的数字在10～25之间时，g为1，否则为0

            可以用递归的方式计算，但是会有重叠的子问题，因此从右到左计算，使用数组将每步计算的值存储起来

        """

        if number < 0:
            return 0
        # 将数字转化成字符串
        numberInString = str(number)

        return self.GetTranslationCountCore(numberInString)

    def GetTranslationCountCore(self, number):
        length = len(number)
        # counts数组存放，从每一个字符开始的翻译数目f(i)
        counts = [0] * length
        count = 0
        # 从右到左开始翻译
        for i in range(length-1, -1, -1):
            count = 0
            if i < length - 1:
                # f(i) = f(i+1)
                count = counts[i+1]
            else:
                # 如果是最后一个字符
                count = 1

            if i < length - 1:
                # 判断第i位和第i+1位数字是否在10～25的范围内，若不再，则不加
                digit1 = int(number[i])
                digit2 = int(number[i+1])
                converted = digit1 * 10 + digit2
                if 10 <= converted <= 25:
                    if i < length - 2:
                        count += counts[i+2]
                    else:
                        # 如果是倒数第2位，则加1
                        count += 1
            # 计算出f(i)
            counts[i] = count

        count = counts[0]

        return count


