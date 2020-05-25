"""
在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。
你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。
给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

示例 1:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 12
解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物

"""


class Solution:
    def maxValue(self, grid):
        # 首先判断输入是否合法
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        dp = [[0 for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                up = left = 0
                if i > 0:
                    up = dp[i-1][j]
                if j > 0:
                    left = dp[i][j-1]

                dp[i][j] = max(up, left) + grid[i][j]

        return dp[rows-1][cols-1]


if __name__ == '__main__':
    grid = [[1,3,1],
            [1,5,1],
            [4,2,1]]
    res = Solution().maxValue(grid)
    print(res)