"""
题目描述
操作给定的二叉树，将其变换为源二叉树的镜像。

输入描述:
二叉树的镜像定义：
        源二叉树
    	    8
    	   /  \
    	  6   10
    	 / \  / \
    	5  7 9 11

    	镜像二叉树
    	    8
    	   /  \
    	  10   6
    	 / \  / \
    	11 9 7  5

"""


class Solution1:
    def Mirror(self, root):
        """
        【递归法】
            通过画图比较原二叉树和镜像二叉树的区别，可以看出，镜像二叉树就是将二叉树的每个非叶结点的左右结点交换位置
            因此我们可以采用前序遍历的顺序遍历二叉树，当遇到非叶结点时，就交换他们的左右结点，递归出口时遇到叶子结点，返回None

        :param root:
        :return:
        """
        if not root:
            return

        # 递归出口：遇到叶结点
        if not root.left and not root.right:
            return

        # 交换左右子结点
        temp = root.left
        root.left = root.right
        root.right = temp

        # 递归左子树
        if root.left:
            self.Mirror(root.left)
        # 递归右子树
        if root.right:
            self.Mirror(root.right)


class Solution2:
    def Mirror(self, root):
        if not root:
            return

        stackNode = []
        stackNode.append(root)

        while len(stackNode) > 0:
            nodeNum = len(stackNode) - 1
            tree = stackNode[nodeNum]
            stackNode.pop()
            nodeNum -= 1
            if tree.left != None or tree.right != None:
                tree.left, tree.right = tree.right, tree.left
            if tree.left:
                stackNode.append(tree.left)
                nodeNum += 1
            if tree.right:
                stackNode.append(tree.right)
                nodeNum += 1
