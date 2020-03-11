class Solution:
    def towSum(self, n):
        if n <= 0:
            return []
        dp = [0] * 70
        for i in range(1, 7):
            dp[i] = 1

        for i in range(2, n+1):
            for j in range(6*i, i-1, -1):
                dp[j] = 0
                for cur in range(1, 7):
                    if j - cur < i-1:
                        break
                    dp[j] += dp[j-cur]

        all = pow(6, n)
        result = []
        for i in range(n, 6*n+1):
            result.append(dp[i] * 1.0 / all)
        return result