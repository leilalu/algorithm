"""
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

"""


class Solution:
    def verifyPostorder(self, postorder):
        if not postorder:
            return True

        root = postorder[-1]

        for i in range(len(postorder)):
            if postorder[i] > root:
                break

        for j in range(i, len(postorder)):
            if postorder[j] < root:
                return False
        left = right = True
        if i > 0:
            left = self.verifyPostorder(postorder[:i])

        if i < len(postorder) - 1:
            right = self.verifyPostorder(postorder[i:-1])

        return left and right