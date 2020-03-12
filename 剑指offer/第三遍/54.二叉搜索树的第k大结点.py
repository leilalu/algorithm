class Solution:
    def kthLargest(self, root,  k):
        if not root:
            return None

        inorder = []
        def getInOrder(root):
            if root.left:
                getInOrder(root.left)
            inorder.append(root.val)
            if root.right:
                getInOrder(root.right)

        getInOrder(root)

        inorder = inorder[::-1]

        if k > len(inorder):
            return None
        else:
            return inorder[k-1]