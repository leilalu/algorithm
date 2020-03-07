"""
题目描述

输入一个整数数组，判断该数组是不是某二叉搜索树的前序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。

"""


class Solution:
    def VerifySquenceOfBST(self, preorder):
        if not preorder:
            return True

        root = preorder[0]

        # 查找左子树
        for i in range(1, len(preorder)):
            if preorder[i] > root:
                break

        # 查找右子树
        for j in range(i, len(preorder)):
            if preorder[i] < root:
                return False

        left = right = True
        # 是否存在左子树
        if i > 1:
            left = self.VerifySquenceOfBST(preorder[1:i])
        # 是否存在右子树
        if i < len(preorder):
            right = self.VerifySquenceOfBST(preorder[i:])

        return left and right

if __name__ == '__main__':
    sequence = [8, 6, 5, 7, 10, 9, 11]
    s = Solution()
    res = s.VerifySquenceOfBST(sequence)
    print(res)