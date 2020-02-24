"""
题目描述

输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def VerifySquenceOfBST(self, sequence):
        """
            递归法

            在后续遍历得到的序列中，最后一个数字是树的根结点。
            数组前面的数字可以分为两部分：第一部分是左子树结点的值，它们都比根结点的值小
                                      第二部分是右子树结点的值，它们逗比根结点的值大

        :param sequence:
        :return:
        """
        # 检查无效输入
        if not sequence:
            return False

        # 根结点
        root = sequence[-1]
        # 判断左子树
        for i in range(len(sequence)):
            if sequence[i] > root:
                break
        # 判断右子树
        for j in range(i, len(sequence)):
            if sequence[j] < root:
                return False

        left = right = True
        # 存在左子树
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[:i])
        # 存在右子树
        if i < len(sequence) - 1:
            right = self.VerifySquenceOfBST(sequence[i:-1])

        return left and right


if __name__ == '__main__':
    sequence = [5,9,11,10,8]
    s = Solution()
    res = s.VerifySquenceOfBST(sequence)
    print(res)

