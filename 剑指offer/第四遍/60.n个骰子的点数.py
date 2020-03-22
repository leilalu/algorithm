"""
把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。



你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。



示例 1:

输入: 1
输出: [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]
示例 2:

输入: 2
输出: [0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,0.11111,0.08333,0.05556,0.02778]

"""


class Solution:
    def twoSum(self, n):
        dp = [0] * 70

        for i in range(1, 7):
            dp[i] = 1

        for i in range(2, n+1):
            for j in range(6*i, i-1, -1):
                dp[j] = 0
                for cur in range(1, 7):
                    if j - cur < i - 1:
                        break
                    else:
                        dp[j] += dp[j-cur]

        all = pow(6, n)
        result = []
        for i in range(n, 6*n+1):
            result.append(dp[i] * 1.0 / all)
        return result


if __name__ == '__main__':
    n = 2
    res = Solution().twoSum(n)
    print(res)


