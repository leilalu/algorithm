"""
数字以0123456789101112131415…的格式序列化到一个字符序列中。
在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。

请写一个函数，求任意第n位对应的数字。



示例 1：

输入：n = 3
输出：3
示例 2：

输入：n = 11
输出：0

"""


class Solution:
    def findNthDigit(self, n):
        if n < 0:
            return None

        digit = 1
        digitCount = self.getDigitCount(digit)
        while n >= digitCount * digit:
            n -= digitCount * digit
            digit += 1
            digitCount = self.getDigitCount(digit)

        return self.findNumber(n, digit)

    def getDigitCount(self, digit):
        if digit == 1:
            return 10
        return 9 * (10 ** (digit-1))

    def startNumber(self, digit):
        if digit == 1:
            return 0
        return 10 ** (digit-1)

    def findNumber(self, n, digit):
        start = self.startNumber(digit)
        number = start + n // digit
        lost = digit - n % digit

        for i in range(lost-1):
            number = number // 10

        return number % 10


if __name__ == '__main__':
    n = 100
    res = Solution().findNthDigit(n)
    print(res)
