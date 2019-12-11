"""
二叉树的结构、存储、先序、中序、后序遍历（递归+迭代）

"""


class TreeNode:
    # 二叉树的结点
    def __init__(self, x):
        self.val = x
        self.left = None  # 左子树
        self.right = None  # 右子树


# 先序遍历(递归)
def preTraversal(root):
    res = []

    def helper(root):
        if not root:
            return
        res.append(root.val)
        helper(root.left)
        helper(root.right)

    helper(root)
    return res


# 中序遍历(递归)
def midTraverasal(root):
    res = []

    def helper(root):
        if not root:
            return
        helper(root.left)
        res.append(root.val)
        helper(root.right)

    helper(root)
    return res


# 后序遍历(递归)：
def afterTraveral(root):
    res = []

    def helper(root):
        if not root:
            return
        helper(root.left)
        helper(root.right)
        res.append(root.val)

    helper(root)
    return res


# 先序遍历(迭代)
def preTraversal_1(root):
    res = []
    if not root:
        return res
    stack = [root]
    while stack:
        root = stack.pop()
        res.append(root.val)
        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)

    return res


# 中序遍历(迭代)
def inorderTraversal_1(root):
    res = []
    stack = []

    p = root

    while p or stack:
        while p:
            stack.append(p)
            p = p.left
        p = stack.pop()
        res.append(p.val)
        p = p.right

    return res

# 后序遍历(迭代)



root = TreeNode(1)
first = TreeNode(2)
root.right = first
second = TreeNode(3)
first.left = second

res = preTraversal(root)
print(res)
