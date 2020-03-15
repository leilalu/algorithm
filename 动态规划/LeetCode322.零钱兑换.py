"""
给定不同面额的硬币 coins 和一个总金额 amount。
编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

示例 1:

输入: coins = [1, 2, 5], amount = 11
输出: 3
解释: 11 = 5 + 5 + 1
示例 2:

输入: coins = [2], amount = 3
输出: -1
说明:
你可以认为每种硬币的数量是无限的。

"""


class Solution:
    def coinChange(self, coins,  amount):
        # 因为求的是最小操作，所以初始化一个大的数，所有的硬币个数都不会超过amount+1个，因此把它初始化为amount+1
        dp = [amount+1] * (amount+1)
        # base case
        dp[0] = 0
        for i in range(amount+1):
            for coin in coins:
                # 只有到硬币面值小于所需面值时，才能选用该硬币
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin] + 1)

        # 如果没有硬币也可以用的话，dp数组没有更改过
        if dp[amount] == amount+1:
            return -1

        return dp[amount]


if __name__ == '__main__':
    coins = [1,2,5]
    amount = 11
    res = Solution().coinChange(coins, amount)
    print(res)

