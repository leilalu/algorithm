class Solution:
    def BinarytreeDepth(self, pRoot):
        depth = 0
        if not pRoot:
            return depth

        left = self.BinarytreeDepth(pRoot.left)
        right = self.BinarytreeDepth(pRoot.right)

        if left > right:
            depth = left + 1
        else:
            depth = right + 1

        return depth

    def IsBalance(self, pRoot):
        if not pRoot:
            return True
        left = self.BinarytreeDepth(pRoot.left)
        right = self.BinarytreeDepth(pRoot.right)

        diff = left - right
        if diff > 1 or diff < -1:
            return False

        return self.IsBalance(pRoot.left) and self.IsBalance(pRoot.right)