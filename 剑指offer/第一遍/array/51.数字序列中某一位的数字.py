"""
题目描述

数字以0123456789101112131415……的格式序列化到一个字符序列中。
在这个序列中，第5位（从0开始计数）是5，第13位是1，第19位是4，等等，倾斜一个函数，求任意第n位对应的数字。

"""


class Solution:
    def digitAtIndex(self, index):
        if index < 0:
            return - 1

        digits = 1  # 位数
        while True:
            numbers = self.countOfIntegers(digits)
            if index < numbers * digits:
                return self.digitAtIndexCore(index, digits)

            index -= digits * numbers
            digits += 1

        return -1

    def countOfIntegers(self, digits):
        """"
            digits位的数字有多少个
        """
        if digits == 1:
            return 10

        count = int(pow(10, digits - 1))

        return 9 * count

    def digitAtIndexCore(self, index, digits):
        """"
            在digits位中的具体哪一个数的哪一个位置
        """
        number = self.beiginNumber(digits) + index / digits

        indexFromRight = digits - index % digits
        for i in range(1, indexFromRight):
            number /= 10

        return number % 10

    def beiginNumber(self, digits):
        """"
            计算digits位数的起始数字
        """
        if digits == 1:
            return 0
        return int(pow(10, digits-1))
