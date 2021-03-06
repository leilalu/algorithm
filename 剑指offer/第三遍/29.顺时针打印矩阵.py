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
        if not matrix or len(matrix)<= 0:
            return []

        rows = len(matrix)
        cols = len(matrix[0])

        start = 0
        res = []

        while rows > start * 2 and cols > start * 2:
            endY = cols - start - 1
            endX  = rows - start - 1

            for i in range(start, endY+1):
                res.append(matrix[start][i])

            if endX > start:
                for i in range(start+1, endX+1):
                    res.append(matrix[i][endY])

            if endX > start and endY > start:
                for i in range(endY-1, start-1, -1):
                    res.append(matrix[endX][i])

            if endX - start > 1 and endY > start:
                for i in range(endX-1, start, -1):
                    res.append(matrix[i][start])

            start += 1

        return res
