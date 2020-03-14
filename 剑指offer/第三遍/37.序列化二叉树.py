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
        result = []
        if not root:
            return ['#']

        stack = []
        while root or stack:
            while root:
                result += [root.val]
                stack.append(root)
                root = root.left

            result += ['#']
            root = stack.pop()
            root = root.right

        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        """
        tree, sp = self.helpDeserialize(data, 0)
        return tree

    def helpDeserialize(self, data, sp):
        # 也应该按照前序遍历的顺序构建左右结点
        if sp >= len(data) or data[sp] == '#':
            return None, sp+1

        node = TreeNode(int(data[sp]))
        sp += 1
        node.left, sp = self.helpDeserialize(data, sp)
        node.right, sp = self.helpDeserialize(data, sp)

        return node, sp