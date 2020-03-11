"""
题目描述

给你一根长度为n的绳子，请把绳子剪成整数长的m段（m、n都是整数，n>1并且m>1），
每段绳子的长度记为k[0],k[1],...,k[m]。
请问k[0]xk[1]x...xk[m]可能的最大乘积是多少？

例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

"""


class Solution1:
    def cutRope(self, number):
        """
            这是一道常规的动态规划题：
                定义函数f(n)为 把长度为n的绳子剪成若干段后各段长度乘积的最大值， 即目标问题
                分析：在剪第一刀时，我们有 n-1 种可能的选择，也就是剪出来的第一段绳子的可能的长度分别是1，2，3,...., n-1
                因此 f(n) = max(f(i) * f(n)) 其中i = 1，。。。n-1

        :param number: 绳子的长度
        :return:
        """
        dp = [0] * (number+1)
        dp[1] = 1
        for i in range(2, number+1):
            for j in range(1, i//2+1):
                dp[i] = max(dp[i], dp[j] * dp[i-j])

            if i != number:  # 在i较小时比较关键
                dp[i] = max(dp[i], i)

        return dp[number]


class Suolution2:
    def cutRope(self, number):
        if number < 2:
            return 0
        if number == 2:
            return 1
        if number == 3:
            return 2

        # 尽可能多的减去长度为3的绳子
        timesOf3 = number // 3  # 有几个3

        # 当绳子最后剩下的时长度为4时，不能再减去长度为3的绳子
        # 此时更好的办法是把绳子剪成长度为2的两段 因为 2*2 > 3*1
        if (number - timesOf3 * 3) == 1:
            timesOf3 -= 1

        timesOf2 = (number - timesOf3 * 3) // 2

        return pow(3, timesOf3) * pow(timesOf2)




if __name__ == '__main__':
    number = 8
    s = Solution1()
    res = s.cutRope(number)
    print(res)