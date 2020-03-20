"""
输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。

例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。



示例 1：

输入：n = 12
输出：5
示例 2：

输入：n = 13
输出：6


"""


class Solution:
    def countDigitOne(self, n):
        if n < 0:
            return 0

        count = 0
        digit = 1
        while n // digit != 0:
            high = n // (digit * 10)
            cur = (n // digit) % 10
            low = n - (n // digit) * digit

            if cur == 0:
                count += high * digit
            elif cur == 1:
                count += high * digit + low + 1
            else:
                count += (high + 1) * digit

            digit *= 10

        return count


if __name__ == '__main__':
    n = 20
    res = Solution().countDigitOne(n)
    print(res)

