"""
把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。

 

你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。


"""


class Solution:
    def twoSum(self, n):
        if n <= 0:
            return []

        dp = [0] * (6 * n)
        for i in range(7):
            dp[i] = 1

        for i in range(2, n+1):
            for j in range(6*n, i-1, -1):
                dp[j] = 0
                for cur in range(1,7):
                    if j-cur < i-1:
                        break
                    dp[j] += dp[j-cur]

        all = pow(6, n)
        result = []
        for i in range(n, 6*n+1):
            result.append(dp[i] * 1.0 / all)
        return result

