"""
题目描述
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def reConstructBinaryTree(self, pre, tin):
        """
            二叉树的先根遍历序列和中根遍历序列可以用于重构二叉树
            先根遍历序列中，第一个元素一定是根节点，对应中根遍历序列中间的一个节点i，那么i左边的就是左子树，i右边的就是右子树。
            接下来分别对左子树和右子树进行递归。左子树：先根序列变为[1:i+1],中根序列变为[:i]   先根序列的取值范围划分可以通过左子树有几个元素解释
                                           右子树：先根序列变为[i+1:], 中根序列变为[i+1:]

        :param pre:
        :param tin:
        :return:
        """
        if not pre and not tin:
            return None
        if set(pre) != set(tin):
            return None

        root = TreeNode(pre[0])
        i = tin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre=pre[1:i+1], tin=tin[:i])
        root.right = self.reConstructBinaryTree(pre=pre[i+1:], tin=tin[i+1:])
        return root


if __name__ == '__main__':
    s = Solution()
