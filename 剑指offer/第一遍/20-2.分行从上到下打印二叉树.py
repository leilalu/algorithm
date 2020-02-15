"""
题目二：分行从上到下打印二叉树

从上到下按层打印二叉树，同一层的结点按从左到右的顺序打印，每一层打印一行。

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def PrintFromTopToBottom(self, pRoot):
        """
            由于要打印多行，所以要设置两个变量，分别记录当前层的结点数量和下一层的结点数量。
            当当前层的数量为0时，将该层结点序列保存起来，将下一层结点数量赋值给当前层结点数量，令下一层结点数量为0，如此循环
            需要注意的是，最后一层都pop完之后，马上判断当前结点数是否为0，否则将会跳出 while queue:的循环

        :param pRoot:
        :return:
        """

        if not pRoot:
            return []

        deque = []
        deque.append(pRoot)
        nextLevel = 0
        thisLevel = 1

        result= []
        level = []
        while deque:
            node = deque.pop(0)
            level.append(node.val)
            thisLevel -= 1

            if node.left:
                deque.append(node.left)
                nextLevel += 1
            if node.right:
                deque.append(node.right)
                nextLevel += 1

            if thisLevel == 0:
                result.append(level)
                level = []
                thisLevel = nextLevel
                nextLevel = 0

        return result


