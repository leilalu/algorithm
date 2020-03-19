"""
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

示例:

给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度  2.

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def minDepth(self, root):
        """"
            递归的深度优先遍历求解：
                找出所有的二叉树的路径，返回路径里最小的深度

            时间复杂度：我们访问每个节点一次，时间复杂度为 O(N) ，其中 N 是节点个数。
            空间复杂度：
                最坏情况下，整棵树是非平衡的，例如每个节点都只有一个孩子，递归会调用 N（树的高度）次，因此栈的空间开销是 O(N) 。
                但在最好情况下，树是完全平衡的，高度只有log(N)，因此在这种情况下空间复杂度只有 O(log(N)) 。


        """

        if not root:
            return 0

        path = []
        self.getPathLength(root, 0, path)

        return min(path)

    def getPathLength(self, root, pathLength, path):
        if not root.left and not root.right:
            # 注意！pathLength是
            path.append(pathLength+1)
            return

        if root.left:
            self.getPathLength(root.left, pathLength+1, path)

        if root.right:
            self.getPathLength(root.right, pathLength+1, path)


class Solution2:
    def minDepth(self, root):
        """"
            迭代的深度优先遍历求解：

            时间复杂度：每个节点恰好被访问一遍，复杂度为 O(N)。
            空间复杂度：最坏情况下我们会在栈中保存整棵树，此时空间复杂度为 O(N)。

        """

        if not root:
            return 0
        else:
            stack, min_depth = [(1, root), ], float('inf')

        while stack:
            depth, root = stack.pop()
            if not root.left and not root.right:
                min_depth = min(depth, min_depth)

            if root.left:
                stack.append((depth+1, root.left))

            if root.right:
                stack.append((depth+1, root.right))

        return min_depth


class Solution3:
    def minDepth(self, root):
        """"
            层次遍历（广度优先遍历）：
                遍历到的第一个叶子结点的深度就是我们要的
                因此采用的是队列

            时间复杂度：
                最坏情况下，这是一棵平衡树，我们需要按照树的层次一层一层的访问完所有节点，除去最后一层的节点。这样访问了 N/2 个节点，因此复杂度是 O(N)。

            空间复杂度：和时间复杂度相同，也是 O(N)。

        """
        from collections import deque
        if not root:
            return 0
        else:
            queue = deque([(1, root)])

        while deque:
            depth, root = queue.popleft()  # 使用deque，实现在O(1)的时间内将元素出队

            if not root.left and not root.right:
                return depth

            if root.left:
                queue.append((depth+1, root.left))

            if root.right:
                queue.append((depth+1, root.right))


class Solution4:
    def minDepth(self, root):
        if not root:
            return 0

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        # 需要注意当只有一个子结点的时候，最大深度应该是有结点的+1，因为空不算叶子结点
        if left == 0:
            return right + 1
        if right == 0:
            return left + 1

        if left < right:
            depth = left + 1
        else:
            depth = right + 1

        return depth

