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

        def helper(node, up_limit=float('inf'), down_limit=float('-inf')):
            if not node:
                return True

            val = node.val
            if val <= down_limit or val >= up_limit:
                return False

            # 右子结点的下界是根结点的值
            if not helper(node.right, up_limit, val):
                return False

            # 左子结点的上界是根结点的值
            if not helper(node.left, val, down_limit):
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

        # 栈里保存一个结点以及该结点时，上界和下界
        stack = [(root, float('inf'), float('-inf'))]

        while stack:
            root, up_limit, down_limit = stack.pop()
            if not root:
                continue

            val = root.val
            # 跟上下界比较，不需要跟它的根结点比较
            if val <= down_limit or val >= up_limit:
                return False

            # 右子结点，没有上界，下界是根结点的值
            stack.append((root.right, up_limit, val))
            # 左子结点，没有下届，上界是根结点的值
            stack.append((root.left, val, down_limit))

        return True


class Solution4:
    def isValidBST(self, root):
        """"
            迭代的中序遍历
        """
        stack, inorder = [], float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()

            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right

        return True










