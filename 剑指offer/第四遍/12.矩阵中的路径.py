"""
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。

路径可以从矩阵中的【任意一格开始】，每一步可以在矩阵中向左、右、上、下移动一格。

如果一条路径经过了矩阵的某一格，那么该路径【不能再次进入该格子】。

例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。

[["a","b","c","e"],
["s","f","c","s"],
["a","d","e","e"]]

但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。



示例 1：

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
示例 2：

输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false

"""


class Solution:
    def exist(self, board, word):
        if not board or not word:
            return False

        rows = len(board)
        cols = len(board[0])

        visited = [[False for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if self.existCore(board, rows, cols, i, j, word, 0, visited):
                    return True
        return False

    def existCore(self, board, rows, cols, row, col, word, wordIndex, visited):
        # 递归停止条件
        if wordIndex == len(word):
            return True
        hasPath = False
        if 0 <= row < rows and 0 <= col < cols and board[row][col] == word[wordIndex] and not visited[row][col]:
            visited[row][col] = True

            hasPath = self.existCore(board, rows, cols, row, col-1, word, wordIndex + 1, visited) or \
                      self.existCore(board, rows, cols, row, col+1, word, wordIndex + 1, visited) or \
                      self.existCore(board, rows, cols, row-1, col, word, wordIndex + 1, visited) or \
                      self.existCore(board, rows, cols, row+1, col, word, wordIndex + 1, visited)

            if not hasPath:
                wordIndex -= 1   # 注意索引要回退一步！！！！！
                visited[row][col] = False

        return hasPath


if __name__ == '__main__':
    board =[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    res = Solution().exist(board, word)
    print(res)