"""
题目二：平衡二叉树

输入一棵二叉树的根结点，判断该树是不是平衡二叉树。
如果某二叉树中任意结点的左、右子树的深度相差不超过1，那么它就是一棵平衡二叉树

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def IsBalanced_Solution(self, pRoot):
        """
            在遍历树的每个节点的时候，分别计算以该节点的左右子结点为根结点的树的深度，如果每个节点的左右子树深度相差不超过1，就是平衡二叉树

            缺点：一个节点会被重复遍历，时间效率不高

        """

        if not pRoot:
            return True

        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)

        diff = left - right

        if diff > 1 or diff < -1:
            return False

        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)

    def TreeDepth(self, pRoot):
        """
            计算树的深度

        """
        depth = 0
        if not pRoot:
            return depth

        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)

        if left > right:
            depth = left + 1
        else:
            depth = right + 1

        return depth


class Solution2:

    def depth(self, pRoot):
        if not pRoot:
            return 0
        left = self.depth(pRoot.left)
        if left == -1:
            return -1  # 如果发现子树不平衡之后就没有必要进行下面的高度的求解了

        right = self.depth(pRoot.right)
        if right == -1:
            return -1  # 如果发现子树不平衡之后就没有必要进行下面的高度的求解了
        if left - right < -1 or left - right > 1:
            return -1
        else:
            if left > right:
                return 1 + left
            else:
                return 1 + right

    def IsBalanced_Solution(self, pRoot):
        return self.depth(pRoot) != -1

