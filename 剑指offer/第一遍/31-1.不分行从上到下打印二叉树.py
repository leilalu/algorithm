"""
题目一：从上到下打印二叉树

从上到下打印二叉树的每个节点，同一层的结点按照从左到右的顺序打印

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def PrintFromTopToBottom(self, root):
        """
            本题重点在于我们要推演出打印二叉树结点的过程
            
            使用队列保存树的结点

            首先将根结点入队，每出队一个节点，现将其从队列中移出，加入返回列表中，
            再判断它有没有左子结点，有没有右子结点，依次入队
            直到队列为空

        :param root:
        :return:
        """
        queue = []
        if not root:
            return []

        result = []
        queue.append(root)

        while len(queue) > 0:
            currentRoot = queue.pop(0)
            result.append(currentRoot.val)
            if currentRoot.left:
                queue.append(currentRoot.left)
            if currentRoot.right:
                queue.append(currentRoot.right)
        return result
