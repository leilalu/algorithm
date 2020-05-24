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
        if not root:
            return []

        preOrder = []
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

        return preOrder

    def deserialize(self, data):
        tree, sp = self.help_deserialize(data, 0)
        return tree

    def help_deserialize(self, data, position):
        # 短路或
        if position >= len(data) or data[position] == '#':
            return None, position+1

        node = TreeNode(int(data[position]))  # 一定要加int，否则会报【内部出错】
        position += 1
        node.left, position = self.help_deserialize(data, position)
        node.right, position = self.help_deserialize(data, position)

        return node, position



