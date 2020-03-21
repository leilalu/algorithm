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
        """
        if not root:
            return []

        preOrder = []

        def getPreOrder(root):
            if not root:
                return []
            stack = []
            while stack or root:
                while root:
                    stack.append(root)
                    preOrder.append(root.val)
                    root = root.left
                    if not root:
                        preOrder.append('#')
                if stack:
                    root = stack.pop()
                    root = root.right
                    if not root:
                        preOrder.append('#')

            getPreOrder(root)

            return ''.join(preOrder)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        """
        tree, sp = self.helpDeserialize(data, 0)
        return tree

    def helpDeserialize(self, data, position):
        if position >= len(data) or data[position] == '#':
            return None, position+1

        node = TreeNode(int(data[position]))
        position += 1
        node.left, position = self.helpDeserialize(data, position)
        # 此时传入的position是发生变化的
        node.right, position = self.helpDeserialize(data, position)

        return node, position
























