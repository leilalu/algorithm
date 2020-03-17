"""
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。
一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），
也不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。
请问该机器人能够到达多少个格子？


示例 1：

输入：m = 2, n = 3, k = 1
输出：3

示例 1：

输入：m = 3, n = 1, k = 0
输出：1

"""


class Solution:
    def movingCount(self, m, n, k):
        if m <= 0 or n <= 0 or k < 0:
            return 0
        visited = [[False for _ in range(n)] for _ in range(m)]

        count = self.movingCountCore(m, n, 0, 0, k, visited)
        return count

    def movingCountCore(self, rows, cols, row, col, k, visited):
        count = 0
        if 0 <= row < rows and 0 <= col < cols and (self.digitSum(row) + self.digitSum(col)) <= k and not visited[row][col]:
            visited[row][col] = True
            count = 1 + self.movingCountCore(rows, cols, row, col+1, k, visited) \
                      + self.movingCountCore(rows, cols, row+1, col, k, visited)

        return count

    def digitSum(self, num):
        sumValue = 0
        while num > 0:
            sumValue += num % 10
            # 注意一定要做整除！！！！！！！！！！！
            num = num // 10
        return sumValue



if __name__ == '__main__':
    m = 1
    n = 2
    k = 1
    res = Solution().movingCount(m, n, k)
    print(res)