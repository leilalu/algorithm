"""
请实现两个函数，分别用来序列化和反序列化二叉树。

示例: 

你可以将以下二叉树：

    1
   / \
  2   3
     / \
    4   5

序列化为 "[1,2,3,null,null,4,5]"

"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        result = []
        if not root:
            return ['#']
        stack = []  # 栈记录表遍历过的结点
        while root or stack:
            while root:
                result += [root.val]
                stack.append(root)
                root = root.left

            # 当前结点为空
            result += ['#']
            # 弹出上次遍历过的结点
            root = stack.pop()
            # 取该节点的右结点
            root = root.right

        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        tree, sp = self.helpDeserialize(data, 0)
        return tree

    def helpDeserialize(self, data, sp):
        if sp >= len(data) or data[sp] == '#':
            return None, sp + 1
        node = TreeNode(int(data[sp]))
        sp += 1
        node.left, sp = self.helpDeserialize(data, sp)
        node.right, sp = self.helpDeserialize(data, sp)

        return node, sp







