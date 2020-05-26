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
        if not root:
            return None

        inorder = []

        # 中序遍历
        def getInOrder(root):
            stack = []
            while stack or root:
                while root:
                    stack.append(root)
                    root = root.left

                root = stack.pop()
                inorder.append(root.val)
                root = root.right

        getInOrder(root)

        if k > len(inorder):
            return None
        else:
            inorder = inorder[::-1]
            return inorder[k-1]




