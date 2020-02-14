"""
题目描述

输入一棵二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # def __init__(self):
    #     self.res = []

    def FindPath(self, root, expectNumber):
        """
            可以看作间接遍历树的问题，使用前序遍历
            但是可以通过减枝，提高时间效率

        :param root:
        :param expectNumber:
        :return:

        """
        res = []
        # 检查无效输入
        if not root:
            return res
        path = []
        currentSum = 0
        self._dfs(root, expectNumber, path, currentSum, res)
        return res

    def _dfs(self, root, expectNumber, path, currentSum, res):
        # 每访问一个节点，就把当前结点添加到路径中去
        currentSum += root.val
        path.append(root.val)

        # 如果是叶结点，并且路径上的值的和等于输入的值，则打印出这条路径
        if not root.left and not root.right and currentSum == expectNumber:
            res.append(path)
        # 如果不是叶结点，则继续访问它的子结点
        if root.left:
            self._dfs(root.left, expectNumber, path, currentSum, res)

        if root.right:
            self._dfs(root.right, expectNumber, path, currentSum, res)

        # 在返回父结点之前，在路径上删除当前结点
        path.pop()

        # 返回二维列表，内部每个列表表示找到的路径



if __name__ == '__main__':
    root = TreeNode(10)
    node1 = TreeNode(5)
    node2 = TreeNode(12)
    node3 = TreeNode(4)
    node4 = TreeNode(7)

    root.left = node1
    root.right = node2

    node1.left = node3
    node1.right = node4

    expectNumber = 22
    s = Solution()
    res = s.FindPath(root, expectNumber)
    print(res)




