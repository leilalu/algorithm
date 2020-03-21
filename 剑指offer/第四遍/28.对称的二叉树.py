"""

请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3



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


class Solution1:
    def isSymmetric(self, root: TreeNode) -> bool:
        """"
            迭代法
            分别求出二叉树的前序遍历序列及其对称前序遍历序列
        """
        if not root:
            return True

        preOrder = []
        mirrorOrder = []

        def getPreOrder(root):
            if not root:
                return []
            stack = []
            while stack or root:
                while root:
                    stack.append(root)
                    preOrder.append(root.val)
                    root = root.left
                    if not root:
                        preOrder.append(None)
                if stack:
                    root = stack.pop()
                    root = root.right
                    if not root:
                        preOrder.append(None)

        def getMirrotOrder(root):
            if not root:
                return []

            stack = []
            while stack or root:
                while root:
                    stack.append(root)
                    mirrorOrder.append(root.val)
                    root = root.right
                    if not root:
                        mirrorOrder.append(None)

                if stack:
                    root = stack.pop()
                    root = root.left
                    if not root:
                        mirrorOrder.append(None)

        getPreOrder(root)
        getMirrotOrder(root)

        return preOrder == mirrorOrder



class Solution2:
    def isSymmetric(self, root: TreeNode) -> bool:
        """"
            递归法
            分别求出二叉树的前序遍历序列和对称前序遍历序列
        """
        if not root:
            return True

        preOrder = []
        mirrorOrder = []

        def getPreOrder(root):
            if not root:
                preOrder.append(None)
            else:
                preOrder.append(root.val)

                getPreOrder(root.left)
                getPreOrder(root.right)

        def getMirrorOrder(root):
            if not root:
                mirrorOrder.append(None)
            else:
                mirrorOrder.append(root.val)

                getMirrorOrder(root.right)
                getMirrorOrder(root.left)

        getPreOrder(root)
        getMirrorOrder(root)

        print(preOrder)
        print(mirrorOrder)

        return preOrder == mirrorOrder


class Solution3:
    def isSymmetric(self, root: TreeNode) -> bool:

        return self.isSymmetricCore(root, root)

    def isSymmetricCore(self, root1, root2):
        if not root1 and not root2:
            # 已经是叶结点了，可以返回了
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False

        return self.isSymmetricCore(root1.left, root2.right) and self.isSymmetricCore(root1.right, root2.left)










































