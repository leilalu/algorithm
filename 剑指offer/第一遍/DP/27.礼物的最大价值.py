"""
题目描述

在一个 m * n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于0）。
你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格，直到达到棋盘的右下角。
给定一个棋盘及其上面的礼物，请计算你最多能拿到多少价值的礼物？

"""


class Solution1:
    def getMaxValue(self, values, rows, cols):
        """
            首先定义 f(i, j) 表示到达(i,j)的格子时能拿到的礼物的总和。题目求的就是f(row-1, col-1)(右下角)
                我们的到f(i,j) 有两种办法，分别是f(i-1,j)（上一行）或者 f(i, j-1)（左边）
                所以 f(i, j) = max(f(i-1,j), f(i, j-1)) + gift[i][j]


        :param values:
        :param rows:
        :param cols:
        :return:
        """
        # 检查无效输入
        if not values or rows <= 0 or cols <= 0:
            return 0
        # 构造二维数组存储到达每个格子能拿到的礼物价值
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

                maxValues[i][j] = max(up, left) + values[i][j]

        # 返回右下角的值
        maxValue = maxValues[rows-1][cols-1]

        return maxValue


class Solution2:
    def getMaxValue(self, values, rows, cols):
        if not values or rows <= 0 or cols <= 0:
            return 0

        maxValues = [0] * cols

        for i in range(rows):
            for j in range(cols):
                left = 0
                up = 0
                if i > 0:
                    up = maxValues[j]  # 上面一行的数字
                if j > 0:
                    left = maxValues[j-1]  # 左边的数字

                maxValues[j] = max(left, up) + values[i][j]

        maxValue = maxValues[cols - 1]

        return maxValue


if __name__ == '__main__':
    values = [[1, 10, 3, 8],
              [12, 2, 9, 6],
              [5, 7, 4, 11],
              [3, 7, 16, 5]]
    rows = 4
    cols = 4

    s = Solution2()
    res = s.getMaxValue(values, rows, cols)
    print(res)

