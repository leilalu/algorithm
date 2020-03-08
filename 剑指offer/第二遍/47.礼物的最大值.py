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
 

提示：

0 < grid.length <= 200
0 < grid[0].length <= 200

"""


class Solution1:
    def maxValue(self, grid):
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])

        # 构造二维数组存放每个位置的最大礼物价值
        maxValues = [0] * rows
        for i in range(rows):
            maxValues[i] = [0] * cols

        for i in range(rows):
            for j in range(cols):
                left = 0
                up = 0

                if i > 0:
                    up = maxValues[i-1][j]
                if j > 0:
                    left = maxValues[i][j-1]

                maxValues[i][j] = max(up, left) + grid[i][j]

        value = maxValues[rows-1][cols-1]
        return value


class Solution2:
    def maxValue(self, grid):
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        maxValues = [0] * cols

        for i in range(rows):
            for j in range(cols):
                left = up = 0
                if i > 0:
                    up = maxValues[j]
                if j > 0:
                    left = maxValues[j-1]

                maxValues[j] = max(up, left) + grid[i][j]

        value = maxValues[cols-1]
        return value


if __name__ == '__main__':
    values = [[1, 10, 3, 8],
              [12, 2, 9, 6],
              [5, 7, 4, 11],
              [3, 7, 16, 5]]
    rows = 4
    cols = 4

    s = Solution2()
    res = s.maxValue(values)
    print(res)

