"""
我们把只包含因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。

示例:

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
说明:

1 是丑数。
n 不超过1690。

"""


class Solution:
    def nthUglyNumber(self, n):
        if n < 1:
            return 0
        dp = [0] * n
        dp[0] = 1
        index2 = 0
        index3 = 0
        index5 = 0
        nextIndex = 1

        while nextIndex < n:
            dp[nextIndex] = self.Min(dp[index2] * 2, dp[index3] * 3, dp[index5] * 5)

            while dp[index2] * 2 <= dp[nextIndex]:
                index2 += 1

            while dp[index3] * 3 <= dp[nextIndex]:
                index3 += 1

            while dp[index5] * 5 <= dp[nextIndex]:
                index5 += 1

            nextIndex += 1

        return dp[-1]

    def Min(self, num1, num2, num3):
        minValue = num1
        if num1 > num2:
            minValue = num2
        if num3 < minValue:
            minValue = num3
        return minValue
