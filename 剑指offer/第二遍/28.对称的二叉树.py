"""
题目描述
请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。

"""


class Solution1:
    def isSymmetrical(self, pRoot):
        return self.isSymmetricalCore(pRoot, pRoot)

    def isSymmetricalCore(self, pRoot1, pRoot2):
        if not pRoot1 and not pRoot2:
            return True
        if not pRoot1 or not pRoot2:
            return False
        if pRoot1.val != pRoot2.val:
            return False

        return self.isSymmetricalCore(pRoot1.left, pRoot2.right) and self.isSymmetricalCore(pRoot1.right, pRoot2.left)


class Solution2:
    def isSymmetrical(self, pRoot):
        preList = self.PreOrder(pRoot)

        mirrorList = self.MirrorOrder(pRoot)

        if preList == mirrorList:
            return True

        return False

    def PreOrder(self, pRoot):
        if not pRoot:
            return [None]
        treeStack = []
        output = []
        pNode = pRoot
        while pNode or len(treeStack) > 0:
            # 根结点存在
            while pNode:
                treeStack.append(pNode)  # 根结点入栈
                output.append(pNode.val)  # 遍历序列加入根结点
                pNode = pNode.left  # 向左结点遍历

                if not pNode:  # 如果左结点不存在，则加入#
                    output.append(None)
            # 如果栈中还有根结点，就pop，看它的右子结点
            if len(treeStack):
                pNode = treeStack.pop()
                pNode = pNode.right
                if not pNode:
                    output.append(None)
        return output

    def MirrorOrder(self, pRoot):

        if not pRoot:
            return [None]

        treeStack = []
        output = []
        pNode = pRoot
        while pNode or len(treeStack) > 0:
            while pNode:
                treeStack.append(pNode)
                output.append(pNode.val)
                pNode = pNode.right

                if not pNode:
                    output.append(None)
            if len(treeStack) > 0:
                pNode = treeStack.pop()
                pNode = pNode.left
                if not pNode:
                    output.append(None)
        return output











