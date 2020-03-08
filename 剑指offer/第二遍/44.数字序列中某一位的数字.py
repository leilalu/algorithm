"""
数字以0123456789101112131415…的格式序列化到一个字符序列中。在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。

请写一个函数，求任意第n位对应的数字。

 

示例 1：

输入：n = 3
输出：3
示例 2：

输入：n = 11
输出：0
 

限制：

0 <= n < 2^31

"""


class Solution:
    def findNthDigit(self, n):
        if n < 0:
            return -1

        digits = 1

        while True:
            count = self.countNumber(digits)
            if n < count * digits:
                return self.findNthDigit(n, digits)

            n -= count * digits
            digits += 1

    def countNumber(self, digits):
        """
            计算digits位的数字有多少个
        """
        if digits == 1:
            return 10

        count = int(pow(10, digits-1))

        return count * 9

    def findNthDigit(self, n, digits):
        number = self.beginNumber(digits) + n // digits

        index = digits - n % digits
        for i in range(1, index):
            number /= 10
        return int(number % 10)


    def beginNumber(self, digits):
        """
            计算第一个digits位数的数字
        """
        if digits == 1:
            return 0

        number = int(pow(10, digits-1))
        return number