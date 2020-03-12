class Solution:
    def maxDepth(self, root):
        depth = 0
        if not root:
            return 0

        left = right = 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        if left < right:
            depth = right + 1
        else:
            depth = left + 1

        return depth