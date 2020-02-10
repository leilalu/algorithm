"""
题目描述
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。

"""


# 树 的数据结构
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def reConstructBinaryTree_1(self, pre, tin):
        """
            很自然想到使用【递归】来做
            前序遍历的第一个元素就是树的根结点，再中序遍历中找到这个数，那么这个数前面的是左子树，右面的是右子树（由于数不重复）
            分别看左子树和右子树，前序遍历的左子树中，第一个元素是根结点，再在中序遍历序列中找到这个结点，划分左右子树
                        接下来分别对左子树和右子树进行递归。左子树：先根序列变为[1:i+1],中根序列变为[:i]   先根序列的取值范围划分可以通过左子树有几个元素解释
                                           右子树：先根序列变为[i+1:], 中根序列变为[i+1:]
        :param pre: 用数组保存的树的前序遍历
        :param tin: 用数组保存的树的后序遍历
        :return: 返回二叉树结构

        """

        if not pre or not tin:
            return None
        if set(pre) != set(tin):  # 判断输入的前序序列和中序序列是否匹配
            return None

        root = TreeNode(pre[0])
        i = tin.index(pre[0])
        root.left = self.reConstructBinaryTree_1(pre=pre[1:i+1], tin=tin[:i])
        root.right = self.reConstructBinaryTree_1(pre=pre[i+1:], tin=tin[i+1:])

        return root








