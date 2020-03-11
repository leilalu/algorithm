class Solution:
    def Lowest(self, root, p, q):
        if not root or not p or not q:
            return None

        while root:
            if p.val <= root.val <= q.val or q.val <= root.val <= p.val:
                return root
            elif p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right

        return None