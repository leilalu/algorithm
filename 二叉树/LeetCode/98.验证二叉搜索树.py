"""
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的【左子树】只包含小于当前节点的数。
节点的【右子树】只包含大于当前节点的数。
所有【左子树】和【右子树】自身必须也是二叉搜索树。

示例 1:

输入:
    2
   / \
  1   3
输出: true
示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def isValidBST(self, root):
        """"
            先得到树的中序遍历序列，再遍历中序序列判断它是否是递增排序的，如果不是，则不是二叉搜索树
        """
        if not root:
            return True
        inorder = []

        def InOrder(root):
            if root.left:
                InOrder(root.left)
            inorder.append(root.val)
            if root.right:
                InOrder(root.right)

        InOrder(root)

        for i in range(len(root)):
            if i > 0:
                if root[i] <= root[i-1]:
                    return False

        return True


class Solution2:
    def isValidBST(self, root):
        """"
            递归法，保留每个节点的上界和下界更新

            时间复杂度：O(N) 每个节点访问一次
            空间复杂度: O(N) 我们跟进了整棵树，递归栈
        """
        def helper(root, lower=float('-inf'), upper=float('inf')):
            # 递归出口
            if not root:
                return True

            val = root.val
            # 本结点处的判断
            if val <= lower or val >= upper:
                return False

            # 子结点处的判断
            # 判断右子结点，并设置下界为根结点的值
            if not helper(root.right, val, upper):
                return False

            # 判断左子结点，并设置上界为根结点的值
            if not helper(root.lert, lower, val):
                return False

            return True

        return helper(root)


class Solution3:
    def isValidBST(self, root):
        """""
            迭代法，深度优先遍历

            时间最快！

        """
        if not root:
            return True

        stack = [(root, float('-inf'), float('inf'))]

        while stack:
            node, lower, upper = stack.pop()
            if not node:
                continue

            # 判断当前结点
            val = node.val
            if val <= lower or val >= upper:
                return False
            # 添加子结点，设置其上界和下界
            stack.append((node.right, val, upper))
            stack.append((node.left, lower, val))

        return True


class Solution4:
    def isValidBST(self, root):
        """"
            迭代的中序遍历
        """

        stack, front = [], float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()

            if root.val <= front:
                return False
            # 更新目前的最小值
            front = root.val
            # 查看右子结点
            root = root.right

        return True
















