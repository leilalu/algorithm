"""
题目描述
地上有一个m行和n列的方格。
一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。

例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。

请问该机器人能够达到多少个格子？

"""


class Solution:
    def movingCount(self, threshold, rows, cols):
        if rows < 1 or cols < 1 or threshold < 0:
            return 0

        visited = [False] * (rows * cols)

        count = self.movingCountCore(threshold, rows, cols, 0, 0, visited)

        return count

    def movingCountCore(self, threshold, rows, cols, row, col, visited):
        # 机器可以到达的格子数
        count = 0

        if self.check(threshold, rows, cols, row, col, visited):
            visited[row * cols + col] = True

            count = 1 + self.movingCountCore(threshold, rows, cols, row+1, col, visited) \
                      + self.movingCountCore(threshold, rows, cols, row-1, col, visited) \
                      + self.movingCountCore(threshold, rows, cols, row, col+1, visited) \
                      + self.movingCountCore(threshold, rows, cols, row, col-1, visited)

        return count

    def check(self, threshold, rows, cols, row, col, visited):
        if 0 <= row < rows and 0 <= col < cols and not visited[row * cols + col] and (self.getDigitSum(row) + self.getDigitSum(col)) <= threshold:
            return True
        return False

    def getDigitSum(self, num):
        sum = 0
        while num > 0:
            sum += num % 10
            num = num // 10

        return sum



if __name__ == '__main__':
    m = 1
    n = 2
    k = 1
    res = Solution().movingCount(m, n, k)
    print(res)