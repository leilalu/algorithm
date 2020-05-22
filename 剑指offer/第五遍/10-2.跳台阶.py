"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：

输入：n = 2
输出：2
示例 2：

输入：n = 7
输出：21

"""


class Solution:
    def numWays(self, n):
        # 首先判断输入是否合法
        if n <= 0:
            return 1

        tmp = [1, 1]
        for i in range(2, n+1):
            tmp[i % 2] = tmp[0] + tmp[1]

        return tmp[n % 2] % 1000000007


if __name__ == '__main__':
    n = 7
    res = Solution().numWays(n)
    print(res)