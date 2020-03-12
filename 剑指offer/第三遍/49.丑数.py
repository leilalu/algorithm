class Solution:
    def nthUglyNumber(self, n):
        if n <= 0:
            return 0
        dp = [1] * n
        nextIndex = 1

        index2 = 0
        index3 = 0
        index5 = 0

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
        if num1> num2:
            minValue = num2
        if num3 < minValue:
            minValue = num3

        return minValue
