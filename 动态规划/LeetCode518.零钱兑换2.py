"""
给定不同面额的硬币和一个总金额。
写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。

示例 1:

输入: amount = 5, coins = [1, 2, 5]
输出: 4
解释: 有四种方式可以凑成总金额:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
示例 2:

输入: amount = 3, coins = [2]
输出: 0
解释: 只用面额2的硬币不能凑成总金额3。
示例 3:

输入: amount = 10, coins = [10]
输出: 1


"""


class Solution:
    def change(self, amount, coins):
        # dp = [0] * (amount+1)
        #
        # dp[0] = 1
        #
        # for coin in coins:
        #     for x in range(coin, amount+1):
        #         dp[x] += dp[x-coin]
        # return dp[amount]

        # dp[i][j] 表示用前i个硬币凑成金额j的组合数
        dp = [[0 for _ in range(amount+1)] for _ in range(len(coins)+1)]
        # base case： 用0个硬币凑成金额0的组合数是1
        dp[0][0] = 1
        # 从第一个硬币开始
        for i in range(1, len(coins)+1):
            # 用第一个硬币凑成金额j
            for j in range(amount+1):
                if j - coins[i-1] >= 0:
                    # 当第i个硬币的金额小于等于金额j时，硬币可以使用，那么使用前i个硬币凑成金额j有两种情况
                    # 一种是不使用硬币i，仅使用前i-1个硬币凑成金额j，一种是使用硬币i，那么之前使用过了硬币i已经凑到了j-第i个硬币的值了，就差硬币i了
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
                else:
                    # 当第i个硬币金额大于金额j的时候，硬币i无法使用，因此，只能靠前i-1个硬币凑成金额j
                    dp[i][j] = dp[i-1][j]

        return dp[-1][-1]


if __name__ == '__main__':
    amount = 5
    coins = [1,2,5]

    res = Solution().change(amount, coins)

    print(res)


