"""
我们把只包含因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。
 

示例:

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
说明:  

1 是丑数。
n 不超过1690。

"""


class Solution:
    def nthUglyNumber(self, n):
        if n <= 0:
            return 0
        dp = [0] * n
        dp[0] = 1

        index_2 = 0
        index_3 = 0
        index_5 = 0
        nextIndex = 1

        while nextIndex < n:
            dp[nextIndex] = self.minNumber(dp[index_2] * 2, dp[index_3] * 3, dp[index_5] * 5)

            while dp[index_2] * 2 <= dp[nextIndex]:
                index_2 += 1

            while dp[index_3] * 3 <= dp[nextIndex]:
                index_3 += 1

            while dp[index_5] * 5 <= dp[nextIndex]:
                index_5 += 1

            nextIndex += 1

        return dp[-1]

    def minNumber(self, num1, num2, num3):
        minValue = num1
        if num2 < num1:
            minValue = num2
        if num3 < minValue:
            minValue = num3

        return minValue


if __name__ == '__main__':
    n = 10
    res = Solution().nthUglyNumber(n)
    print(res)


