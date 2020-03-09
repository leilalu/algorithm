"""
给定一棵二叉搜索树，请找出其中第k大的节点。


示例 1:
输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 4


示例 2:
输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 4

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthLargest(self, root, k):
        if not root or k == 0:
            return None

        treeNode = []

        def InOrder(root):
            if not root:
                return

            if root.left:
                InOrder(root.left)

            treeNode.append(root.val)

            if root.right:
                InOrder(root.right)

        InOrder(root)

        if k > len(treeNode):
            return None
        else:
            treeNode = treeNode[::-1]
            return treeNode[k-1]



