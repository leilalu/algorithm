"""
给定一个二叉树，返回所有从根节点到叶子节点的路径。

说明: 叶子节点是指没有子节点的节点。

示例:

输入:

   1
 /   \
2     3
 \
  5

输出: ["1->2->5", "1->3"]

解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def binaryTreePaths(self, root):
        """"
            迭代法
        """
        if not root:
            return []
        res = []
        stack = [(root, [root.val])]
        while stack:
            node, path = stack.pop()

            if not node.left and not node.right:
                route = ""
                for i in range(len(path)-1):
                    route += path[i] + "->"
                route += path[-1]
                res.append(route)

            if node.right:
                stack.append((node.right, path+[node.right.val]))

            if node.left:
                stack.append((node.left, path+[node.left.val]))

        return res


class Solution2:
    def binaryTreePaths(self, root):
        """"
            递归法
            时间复杂度：每个节点只会被访问一次，因此时间复杂度为 O(N)，其中 N 表示节点数目。
            空间复杂度：O(N)。这里不考虑存储答案 paths 使用的空间，仅考虑额外的空间复杂度。额外的空间复杂度为递归时使用的栈空间，
                        在最坏情况下，当二叉树中每个节点只有一个孩子节点时，递归的层数为 N，此时空间复杂度为 O(N)。
                        在最好情况下，当二叉树为平衡二叉树时，它的高度为 \log(N)，此时空间复杂度为 O(\log(N))。
        """
        if not root:
            return []
        paths = []

        def construct_paths(root, path):
            if root:
                path += str(root.val)

                if not root.left and not root.right:
                    paths.append(path)
                else:
                    path += '->'
                    construct_paths(root.left, path)
                    construct_paths(root.right, path)

        construct_paths(root, '')

        return paths


class Solution3:
    def binaryTreePaths(self, root):
        if not root:
            return []

        paths = []

        stack = [(root, str(root.val))]

        while stack:
            node, path = stack.pop()

            if not node.left and not node.right:
                paths.append(path)
            else:
                if node.left:
                    stack.append((node.left, path + '->' + str(node.left.val)))
                if node.right:
                    stack.append((node.right, path + '->' + str(node.right.val)))

        return paths




