"""
给定一个二叉树，它的每个结点都存放着一个整数值。

找出路径和等于给定数值的路径总数。

路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。

示例：

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

返回 3。和等于 8 的路径有:

1.  5 -> 3
2.  5 -> 2 -> 1
3.  -3 -> 11

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root, sum):
        """"
            双重递归
        """

        if not root:
            return 0

        # 内层递归函数，求从每个结点开始向下找存在的路径个数
        def dfs(root, sum):
            count = 0  # 记录路径个数
            if not root:
                return 0

            # 如果它本身的值就是，说明达到路径底部，路径数加一
            if root.val == sum:
                count += 1

            # 再递归的看左右子树中的路径数
            count += dfs(root.left, sum - root.val)
            count += dfs(root.right, sum - root.val)

            return count

        return dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)









