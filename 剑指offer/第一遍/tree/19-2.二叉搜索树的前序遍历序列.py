"""
题目描述

输入一个整数数组，判断该数组是不是某二叉搜索树的前序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。

"""


class Solution:
    def VerifySquenceOfBST(self, sequence):
        if not sequence:
            return False

        root = sequence[0]
        # 处理左子树
        for i in range(1, len(sequence)):
            if sequence[i] > root:
                break
        # 判断右子树
        for j in range(i, len(sequence)):
            if sequence[j] < root:
                return False

        left = right = True
        # 处理左子树
        if i > 1:
            left = self.VerifySquenceOfBST(sequence[1:i])

        # 处理右子树
        if i < len(sequence):
            right = self.VerifySquenceOfBST(sequence[i:])

        return left and right


if __name__ == '__main__':
    sequence = [8, 6, 5, 7, 10, 9, 11]
    s = Solution()
    res = s.VerifySquenceOfBST(sequence)
    print(res)