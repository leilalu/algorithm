"""
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:
给定的树 A:

     3
    / \
   4   5
  / \
 1   2
给定的树 B：

   4 
  /
 1
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

示例 1：

输入：A = [1,2,3], B = [3,1]
输出：false
示例 2：

输入：A = [3,4,5,1,2], B = [4,1]
输出：true

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubStructure(self, A, B):
        if not A or not B:
            return False

        result = False

        if A.val == B.val:
            result = self.hasSubStructure(A, B)

        # 注意 递归调用子结点的时候，调用的是原函数
        if not result and A.left:
            result = self.isSubStructure(A.left, B)

        if not result and A.right:
            result = self.isSubStructure(A.right, B)

        return result

    def hasSubStructure(self, A, B):
        if not B:
            return True
        if not A:
            return False
        if A.val != B.val:
            return False

        return self.hasSubStructure(A.left, B.left) and self.hasSubStructure(A.right, B.right)




