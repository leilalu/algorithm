"""
请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

 

示例 1：

输入：root = [1,2,2,3,4,4,3]
输出：true
示例 2：

输入：root = [1,2,2,null,3,null,3]
输出：false

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root):
        if not root:
            return True
        self.preOrder = []
        self.preOrderSym = []

        self.getPreOrder(root)
        self.getPreOrderSym(root)

        return True if self.preOrder == self.preOrderSym else False

    def getPreOrder(self, root):
        if not root:
            self.preOrder.append('#')
        else:
            self.preOrder.append(root.val)

            self.getPreOrder(root.left)
            self.getPreOrder(root.right)

    def getPreOrderSym(self, root):
        if not root:
            self.preOrderSym.append('#')
        else:
            self.preOrderSym.append(root.val)

            self.getPreOrderSym(root.right)
            self.getPreOrderSym(root.left)



