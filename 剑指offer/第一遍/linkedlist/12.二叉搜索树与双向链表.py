"""
题目描述
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向。

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Convert(self, pRootOfTree):
        """
            首先分析二叉搜索树与双向链表之间的关系。
            二叉搜索树有两个指针，分别指向左子结点和右子结点；排序的双向链表也有两个指针，分别指向前一个节点和后一个节点（注意：头结点和尾结点只有单向指针）

            在二叉搜索树中，左子结点的值总是小于右子结点的值，右子结点的值总是大于左子结点的值，因此在将二叉搜索树转换成排序双向链表时，
            原先指向左子结点的指针调整为指向前一个结点的指针，原先指向右子结点的指针调整为指向后一个结点的指针。

            由于要求转换之后的链表是排好序的，我们可以用中序遍历树的每个结点，因为中序遍历算法的特点是按照从小到大的顺序遍历二叉树的每个节点。

            当遍历的根结点的时候，根结点将和它左子树中最大的结点连接起来，同时还和它右子树中最小的结点连接起来。
            因此按照中序遍历的顺序，当我们遍历转换到根结点时，左子树已经转换成一个排序的链表了，并且处在链表中的最后一个节点就是当前最大的结点

        :param pRootOfTree:
        :return:
        """

        if not pRootOfTree:
            return None

        # 叶结点
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree

        # 若存在左子结点，则把左子树最大的结点与根结点连接在一起
        if pRootOfTree.left:
            left = pRootOfTree.left
            # 对左子树进行转换，转换的链表头指针在最左
            self.Convert(left)
            # 指向最右端
            while left.right:
                left = left.right
            pRootOfTree.left = left
            left.right = pRootOfTree

        # 若存在右子结点，则把右子树最小的结点与根结点连接在一起
        if pRootOfTree.right:
            right = pRootOfTree.right
            # 对右子树进行转换，转换后的链表头指针在最左
            self.Convert(right)
            # 指向最左端
            while right.left:
                right = right.left
            pRootOfTree.right = right
            right.left = pRootOfTree

        # 找到头结点
        while pRootOfTree.left:
            pRootOfTree = pRootOfTree.left

        return pRootOfTree


if __name__ == '__main__':
    node4 = TreeNode(4)
    node6 = TreeNode(6)
    node8 = TreeNode(8)
    node10 = TreeNode(10)
    node12 = TreeNode(12)
    node14 = TreeNode(14)
    node16 = TreeNode(16)

    node10.left = node6
    node10.right = node14
    node6.left = node4
    node6.right = node8
    node14.left = node12
    node14.right = node16

    s = Solution()
    res = s.Convert(node10)





