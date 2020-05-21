"""
请完成一个函数，输入一个二叉树，该函数输出它的镜像。

例如输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
镜像输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1

 

示例 1：

输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def mirrorTree(self, root):
        from collections import deque
        if not root:
            return None

        queue = deque([root])
        while queue:
            node = queue.popleft()
            left = node.left
            node.left = node.right
            node.right = left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root


class Solution2:
    def mirrorTree(self, root):
        if not root:
            return None
        if not root.left and not root.right:
            return root
        left = root.left
        if left:
            left = self.mirrorTree(left)
        right = root.right
        if right:
            right = self.mirrorTree(right)

        root.left = right
        root.right = left


        
        return root

