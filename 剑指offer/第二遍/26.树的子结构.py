"""
题目描述
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）

"""


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if not pRoot1 or not pRoot2:
            return False

        result = False
        if pRoot1.val == pRoot2.val:
            result = self.hasSubtreeCore(pRoot1, pRoot2)
        if not result and pRoot1.left:
            result = self.hasSubtreeCore(pRoot1.left, pRoot2)
        if not result and pRoot1.right:
            result = self.hasSubtreeCore(pRoot1.right, pRoot2)

        return result

    def hasSubtreeCore(self, pRoot1, pRoot2):
        if not pRoot2:
            return True
        if not pRoot1:
            return False

        if pRoot1.val != pRoot2.val:
            return False

        return self.hasSubtreeCore(pRoot1.left, pRoot2.left) and self.hasSubtreeCore(pRoot1.right, pRoot2.right)