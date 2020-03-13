"""
在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

 

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
        m = len(grid)
        n = len(grid[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                up = left = 0
                if i > 0:
                    up = dp[i-1][j]

                if j > 0:
                    left = dp[i][j-1]

                dp[i][j] = max(up, left) + grid[i][j]

        return dp[m-1][n-1]


if __name__ == '__main__':
    values = [[1, 10, 3, 8],
              [12, 2, 9, 6],
              [5, 7, 4, 11],
              [3, 7, 16, 5]]
    rows = 4
    cols = 4

    s = Solution()
    res = s.maxValue(values)
    print(res)

