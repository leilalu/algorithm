"""
题目描述

输入一棵二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)

"""
"""
深度优先遍历（DFS）的写法：

递归写法：

    def binaryTreePaths(self, root):
        if not root:
            return []
        result = []
        self.DFS(root, result, [root.val])
        return result

    def DFS(self, root, result, path):
        # 判断结点类型
        # 是叶结点
        if not root.left and not root.right:
            result.append(path)
        
        # 是中间结点
        if root.left:
            self.DFS(root.left, result, path + [root.left.val])
        if root.right:
            self.DFS(root.right, result, path + [root.right.val])

非递归写法：

    def binaryTreePaths2(self, root):
        if not root:
            return []
        result = []
        # 非递归则用栈来辅助
        stack = []
        stack.append((root, [root.val]))
        while stack:
            node, path = stack.pop()
            # 判断当前结点类型
            # 是叶结点
            if not node.left and not node.right:
                result.append(path)
            # 是中间结点，进行子结点压栈
            if node.left:
                stack.append((node.left, path + [node.left.val]))

            if node.right:
                stack.append((node.right, path + [node.right.val]))
        
        return result


"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def FindPath(self, root, expectNumber):
        """"
            递归法对二叉树进行深度优先遍历，只不过在判断叶结点的时候，加了一个等不等于某个值的判断条件，DFS框架不变
        """
        result = []
        if not root:
            return result

        self.sums = expectNumber
        self.DFS(root, result, [root.val])
        return result

    def DFS(self, root, result, path):
        if not root.left and not root.right and sum(path) == self.sums:
            result.append(path)
        if root.left:
            self.DFS(root.left, result, path + [root.left.val])
        if root.right:
            self.DFS(root.right, result, path + [root.right.val])


class Solution2:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        """"
            非递归法进行二叉树的深度优先遍历，需要借助栈，另外由于栈，因判断左右子结点的时候，要先右后左
            为了记录到每个结点时的路径，在压栈的时候，不仅要压入结点，还要压入该节点的路径
        """

        if not root:
            return []
        result = []
        stack = []
        stack.append((root, [root.val]))
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right and sum(path) == expectNumber:
                result.append(path)

            # 注意：因为是栈弹出，所以在压栈时要先右后左
            if node.right:
                stack.append((node.right, path + [node.right.val]))
            if node.left:
                stack.append((node.left, path + [node.left.val]))
        return result


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
    s = Solution1()
    res = s.FindPath(root, expectNumber)
    print(res)




