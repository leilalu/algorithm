"""
题目描述
请实现两个函数，分别用来序列化和反序列化二叉树

二叉树的序列化是指：
把一棵二叉树按照某种遍历方式的结果以某种格式保存为字符串，从而使得内存中建立起来的二叉树可以持久保存。
序列化可以基于先序、中序、后序、层序的二叉树遍历方式来进行修改，序列化的结果是一个字符串，
序列化时通过 某种符号表示空节点（#），以 ！ 表示一个结点值的结束（value!）。

二叉树的反序列化是指：根据某种遍历顺序得到的序列化字符串结果str，重构二叉树。

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Serialize(self, root):
        """
            序列化就是一个前序遍历的过程，不同的是None要保存为特殊字符'#'
        """
        result = ''
        if not root:
            return '#'
        stack = []
        while root or stack:
            while root:
                result += str(root.val) + ','
                stack.append(root)
                root = root.left
            result += '#,'
            root = stack.pop()
            root = root.right
        result = result[:-1]

        return result

    def Deserialize(self, s):
        """
            反序列化过程就是根据前序遍历的字符串，读到数字，就生成一个结点，然后分别生成左右结点，如果读到字符，则意味着是None，则返回None

        """
        serialize = s.split(',')
        tree, sp = self.helpDeserialize(serialize, 0)
        return tree

    def helpDeserialize(self, s, sp):
        if sp >= len(s) or s[sp] == '#':
            return None, sp+1
        node = TreeNode(int(s[sp]))
        sp += 1
        node.left, sp = self.helpDeserialize(s, sp)
        node.right, sp = self.helpDeserialize(s, sp)

        return node, sp


