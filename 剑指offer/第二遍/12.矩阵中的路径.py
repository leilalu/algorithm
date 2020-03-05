"""
题目：
请设计一个函数，用来判断一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一格开始，每一步在矩阵中向左、右、上、下移动一格。
如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。

"""


class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # 判断非法输入
        if not matrix or rows < 1 or cols < 1 or not path:
            return False

        # 创建bool数组判断矩阵中每个元素是否被访问过
        visited = [False] * (rows * cols)

        current = 0
        for i in range(rows):
            for j in range(cols):
                if self.hasPathCore(matrix, rows, cols, i, j, path, current, visited):
                    return True

        return False

    def hasPathCore(self, matrix, rows, cols, row, col, path, current, visited):
        if len(path) == current:
            return True

        hasPath = False

        if 0 <= row < rows and 0 <= col < cols and matrix[row * cols + col] == path[current] and not visited[row * cols + col]:
            current += 1
            visited[row * cols + col] = True

            hasPath = self.hasPathCore(matrix, rows, cols, row, col-1, path, current, visited) or \
                      self.hasPathCore(matrix, rows, cols, row, col+1, path, current, visited) or \
                      self.hasPathCore(matrix, rows, cols, row-1, col, path, current, visited) or \
                      self.hasPathCore(matrix, rows, cols, row+1, col, path, current, visited)

            if not hasPath:
                current -= 1
                visited[row * cols + col] = False

        return hasPath


if __name__ == '__main__':
    s = Solution()
    ifTrue = s.hasPath("ABCESFCSADEE", 3, 4, "ABCCED")
    ifTrue2 = s.hasPath("ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS", 5, 8, "SGGFIECVAASABCEHJIGQEM")
    print(ifTrue2)
