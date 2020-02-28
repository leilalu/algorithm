"""
题目描述

请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。

"""


class Solution1:
    def isSymmetrical(self, pRoot):
        """"
        【递归法】
        """

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
        # 计算前序遍历序列
        preList = self.preOrder(pRoot)
        # 计算镜像二叉树的前序遍历序列
        mirrorList = self.mirrorPreOrder(pRoot)
        # 判断是否对称
        if preList == mirrorList:
            return True
        return False

    def preOrder(self, pRoot):
        """
            循环实现二叉树的前序遍历序列

        """
        if not pRoot:
            return [None]
        treeStack = []
        output = []
        pNode = pRoot
        while pNode or len(treeStack) > 0:
            while pNode:
                treeStack.append(pNode)
                output.append(pNode.val)
                pNode = pNode.left

                if not pNode:
                    # 将叶结点的None也加进去
                    output.append(None)

            if len(treeStack):
                pNode = treeStack.pop()
                pNode = pNode.right
                if not pNode:
                    output.append(None)
        return output

    def mirrorPreOrder(self, pRoot):
        """
            循环实现二叉树的对称前序遍历,right和left互换位置即可

        """
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
            if len(treeStack):
                pNode = treeStack.pop()
                pNode = pNode.left
                if not pNode:
                    output.append(None)
        return output