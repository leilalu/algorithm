"""
翻转一棵二叉树。

示例：

输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def invertTree(self, root):
        # if not root:
        #     return None
        #
        # left = root.left
        # root.left = root.right
        # root.right = left
        #
        # self.invertTree(root.left)
        # self.invertTree(root.right)
        #
        # return root


        """"
            递归法求解
                1、递归出口：空结点翻转，还是空结点，返回它本身
                2、递推关系：先翻转左子树，再翻转右子树，最后将左子树和右子树对应根结点的位置对调

            时间复杂度：树的每个结点都要被访问到，因此时间复杂度是O(n)。在翻转之前，无论如何都要访问结点一次，因此时间复杂度最好就是O(n)

            空间复杂度：由于使用递归，最坏情况下栈里要存放O(h)个方法的调用，其中h是树的高度，由于h 小于 n，因此时间复杂度是O(n)

        """
        if not root:
            return root

        # if not root.left and not root.right:
        #     return root

        left = root.left
        if left:
            left = self.invertTree(left)

        right = root.right
        if right:
            right = self.invertTree(right)

        # 翻转
        root.left = right
        root.right = left

        return root


class Solution2:
    def invertTree(self, root):
        """"
            迭代法求解：
                使用队列进行广度优先遍历
                初始状态队列中只有根结点，当队列中还有结点就一直遍历下去
                将根结点出队，将根结点的左右结点交换（对应左右子树交换），再将左右结点入队

                注意空结点不要入队
        """
        if not root:
            return None

        queue = [root]
        while queue:
            current = queue.pop(0)
            # 交换左右结点
            left = current.left
            current.left = current.right
            current.right = left

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return root



