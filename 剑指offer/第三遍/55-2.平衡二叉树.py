class Solution:
    def isBalanced(self, root):
        return self.isBalancedCore(root) != -1

    def isBalancedCore(self, root):
        if not root:
            return 0

        left = self.isBalancedCore(root.left)
        if left == -1:
            return -1

        right = self.isBalancedCore(root.right)
        if right == -1:
            return -1

        diff = left - right
        if diff < -1 or diff > 1:
            return -1
        else:
            if left > right:
                return left + 1
            else:
                return right + 1

