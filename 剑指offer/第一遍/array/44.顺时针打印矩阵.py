"""
题目描述
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.

"""


class Solution:
    def printMatrix(self, matrix):
        if not matrix:
            return

        if matrix == []:
            return []

        start = 0

        columns = len(matrix[0])
        rows = len(matrix)

        result = []

        while columns > start * 2 and rows > start * 2:
            endX = columns - 1 - start  # 终止列号
            endY = rows - 1 - start  # 终止行号

            # 从左到右将数字存入result
            for i in range(start, endX + 1):
                number = matrix[start][i]
                result.append(number)

            # 从上到下将数字存入result
            # 终止行号大于起始行号
            if start < endY:
                for i in range(start + 1, endY + 1):
                    number = matrix[i][endX]
                    result.append(number)

            # 从右到左将数字存入result
            # 终止行号大于起始行号、终止列号大于起始列号
            if start < endX and start < endY:
                for i in range(endX - 1, start - 1, -1):
                    number = matrix[endY][i]
                    result.append(number)

            # 从下到上将数字存入result
            # 终止行号比起始行号至少大2，终止列号大于起始列号
            if start < endX and start < endY - 1:
                for i in range(endY - 1, start, -1):
                    number = matrix[i][start]
                    result.append(number)
            start += 1
        return result


if __name__ == '__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    res = Solution().printMatrix(matrix)
    print(res)


