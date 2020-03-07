"""
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

 

参考以下这颗二叉搜索树：

     5
    / \
   2   6
  / \
 1   3
示例 1：

输入: [1,6,3,2,5]
输出: false
示例 2：

输入: [1,3,2,6,5]
输出: true

"""


class Solution:
    def verifyPostorder(self, postorder):
        if not postorder:
            return False

        root = postorder[-1]

        # 查找左子树
        # 注意也要遍历到最后一个元素（root）
        for i in range(len(postorder)):
            if postorder[i] > root:
                break

        # 查找右子树
        # 注意也要遍历到最后一个元素（root）
        for j in range(i, len(postorder)):
            if postorder[j] < root:
                return False

        left = right = True
        # 如果存在左子树
        if i > 0:
            left = self.verifyPostorder(postorder[:i])

        # 如果存在右子树
        if i < len(postorder)-1:
            right = self.verifyPostorder(postorder[i:-1])

        return left and right


if __name__ == '__main__':
    sequence = [4,6,7,5]
    s = Solution()
    res = s.verifyPostorder(sequence)
    print(res)
