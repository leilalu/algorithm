"""
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:

输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

"""


class Solution1:
    def numTrees(self, n):
        res = 0

        numList = [num for num in range(1, n + 1)]

        res = self.numTreesCore(numList, res)

        return res

    def numTreesCore(self, numList, res):
        if len(numList) == 0:
            return 0
        if len(numList) == 1:
            return 1
        if len(numList) == 2:
            return 2
        tempSum = 0
        for i in range(len(numList)):
            # 找到根结点i
            left = right = 1
            if i > 0:
                left = self.numTreesCore(numList[:i], res)

            if i < len(numList) - 1:
                right = self.numTreesCore(numList[i + 1:], res)

            tempSum += left * right

        res += tempSum

        return res


class Solution2:
    def numTrees(self, n):
        """"
            动态规划
        """
        G = [0] * (n+1)
        G[0] = G[1] = 1

        # 长度为i
        for i in range(2, n+1):
            # 以j为根结点，长度为i的不同二叉树搜索个数
            for j in range(1, i+1):
                G[i] += G[j-1] * G[i - j]

        return G[n]




if __name__ == '__main__':
    n = 19
    res = Solution2().numTrees(n)
    print(res)









