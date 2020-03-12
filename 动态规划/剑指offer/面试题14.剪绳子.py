"""
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），
每段绳子的长度记为 k[0],k[1]...k[m] 。
请问 k[0]*k[1]*...*k[m] 可能的最大乘积是多少？

例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

示例 1：

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36
提示：

2 <= n <= 58

"""


class Solution1:
    def cutRope(self, n):
        """
            这是一道常规的动态规划题：
                定义函数f(n)为 把长度为n的绳子剪成若干段后各段长度乘积的最大值， 即目标问题
                分析：在剪第一刀时，我们有 n-1 种可能的选择，也就是剪出来的第一段绳子的可能的长度分别是1，2，3,...., n-1
                因此 f(n) = max(f(i) * f(n)) 其中i = 1，。。。n-1

        :param number: 绳子的长度
        :return:
        """
        dp = [0] * (n+1)
        dp[1] = 1

        for i in range(2, n+1):
            for j in range(1, i//2+1):
                dp[i] = max(dp[i], dp[j] * dp[i-j])
            if i != n:
                dp[i] = max(dp[i], i)

        return dp[n]


if __name__ == '__main__':
    number = 8
    s = Solution1()
    res = s.cutRope(number)
    print(res)


