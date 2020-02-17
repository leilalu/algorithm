"""
树的常规遍历操作
包括：前序遍历、中序遍历、后续遍历 和宽度/层次优先遍历

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 前序遍历
class PreOrder:
    def preorder_recursive(self, root):
        if not root:
            return []
        res = []

        def preorder(root):
            res.append(root.val)
            if root.left:
                preorder(root.left)
            if root.right:
                preorder(root.right)

        preorder(root)
        return res

    def preorder_cycle(self, root):
        """
            使用栈

        :param root:
        :return:
        """
        stack = []
        res = []
        cur = root
        while stack or cur:
            if cur:
                res.append(cur.val)
                if cur.right:
                    stack.append(cur.right)
                cur = cur.left
            else:
                cur = stack.pop()
        return res


# 中序遍历
class InOrder:
    def inorder_recursive(self, root):
        if not root:
            return []
        res = []

        def inorder(root):
            if root.left:
                inorder(root.left)
            res.append(root.val)
            if root.right:
                inorder(root.right)

        inorder(root)
        return res

    def inorder_cycle(self, root):
        """
            用栈来辅助
        :param root:
        :return:
        """
        stack = []
        res = []
        cur = root
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right

        return res


# 后续遍历
class PostOrder:
    def postorder_recursive(self, root):
        if not root:
            return []
        res = []

        def postorder(root):
            if root.left:
                postorder(root.left)
            if root.right:
                postorder(root.right)
            res.append(root.val)

        postorder(root)
        return res

    def postorder_cycle(self, root):
        stack = []
        res = []
        cur = root
        while stack or cur:
            if cur:
                res.append(cur.val)
                if cur.right:
                    stack.append(cur.left)
                cur = cur.right
            else:
                cur = stack.pop()
        return res[::-1]


# 层次遍历
class LevelOrder:
    def levelorder_recursive(self, root):

        def helper(node, level):
            if not node:
                return
            else:
                sol[level-1].append(node.val)
                if len(sol) == level:  # 遍历到新层时，只有最左边的结点使得等式成立
                    sol.append([])
                helper(node.left, level+1)
                helper(node.right, level+1)
        sol = [[]]
        helper(root, 1)
        return sol[:-1]

    def levelorder_cycle(self, root):
        if not root:
            return []
        res = []
        cur = root
        queue = [cur]
        while queue:
            cur = queue.pop(0)
            res.append(cur.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return res





if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)

    node1.left = node2
    node1.right = node3

    node2.left = node4
    node2.right = node5

    node3.right = node6

    pre = PreOrder()
    res1 = pre.preorder_cycle(node1)
    inorder = InOrder()
    res2 = inorder.inorder_recursive(node1)
    post = PostOrder()
    res3 = post.postorder_cycle(node1)
    level = LevelOrder()
    res4 = level.levelorder_cycle(node1)
    print(res4)

