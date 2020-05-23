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


class Solution1:
    def isSymmetric(self, root):
        if not root:
            return True

        preOrder = []
        preOrderSym = []

        def getPreOrder(root):
            if not root:
                preOrder.append('#')
            else:
                preOrder.append(root.val)

                getPreOrder(root.left)
                getPreOrder(root.right)

        def getPreOrderSym(root):
            if not root:
                preOrderSym.append('#')
            else:
                preOrderSym.append(root.val)

                getPreOrderSym(root.right)
                getPreOrderSym(root.left)


        getPreOrder(root)
        getPreOrderSym(root)

        return True if preOrder == preOrderSym else False


class Solution2:
    def isSymmetric(self, root):
        if not root:
            return True

        preOrder = []
        preOrderSym = []

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

        def getPreOrderSym(root):
            if not root:
                return []

            stack = []

            while stack or root:
                while root:
                    stack.append(root)
                    preOrderSym.append(root.val)
                    root = root.right
                    if not root:
                        preOrderSym.append(None)

                if stack:
                    root = stack.pop()
                    root = root.left
                    if not root:
                        preOrderSym.append(None)

        getPreOrder(root)
        getPreOrderSym(root)

        return preOrderSym == preOrder


class Solution3:
    def isSymmetric(self, root):
        return self.isSymmetricCore(root, root)

    def isSymmetricCore(self, root1, root2):
        # 如果两者均为空，则对称
        if not root1 and not root2:
            return True

        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False

        return self.isSymmetricCore(root1.left, root2.right) and self.isSymmetricCore(root1.right, root2.left)






