"""

输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。

例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。



示例 1：

输入：n = 12
输出：5
示例 2：

输入：n = 13
输出：6


限制：

1 <= n < 2^31

"""


class Solution:
    def countDigitOne(self, n):
        if n < 0:
            return 0
        count = 0
        for i in range(1, n+1):
            count += self.countOf1(i)

        return count

    def countOf1(self, n):
        count = 0
        while n:
            if n % 10 == 1:
                count += 1
            n = n // 10
        return count