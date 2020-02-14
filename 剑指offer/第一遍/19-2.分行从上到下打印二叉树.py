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


