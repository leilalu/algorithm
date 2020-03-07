"""

输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

 

示例 1：

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：

输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
 

限制：

0 <= matrix.length <= 100
0 <= matrix[i].length <= 100

"""


class Solution:
    def spiralOrder(self, matrix):
        # 检查无效输入
        if not matrix:
            return
        if len(matrix) == 0:
            return []

        rows = len(matrix)
        cols = len(matrix[0])

        start = 0
        result = []
        while rows > start * 2 and cols > start * 2:
            result += self.printCircle(matrix, rows, cols, start)
            start += 1

        return result

    def printCircle(self, matrix, rows, cols, start):
        result = []
        endX = cols - start - 1
        endY = rows - start - 1

        # 打印第一步，从左到右打印一行
        for i in range(start, endX+1):
            number = matrix[start][i]
            result.append(number)

        # 打印第二步，从上到下打印一列
        if start < endY:
            for i in range(start+1, endY+1):
                number = matrix[i][endX]
                result.append(number)

        # 打印第三步，从右到左打印一行
        if start < endX and start < endY:
            for i in range(endX-1, start-1, -1):
                number = matrix[endX][i]
                result.append(number)

        # 打印第四步，从下到上打印一列
        if start < endX and start < endY-1:
            for i in range(endY-1, start, -1):
                number = matrix[i][start]
                result.append(number)

        return result



if __name__ == '__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    res = Solution().spiralOrder(matrix)
    print(res)



