"""
输入某二叉树的【前序遍历】和【中序遍历】的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都【不含重复的数字】。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
 

限制：

0 <= 节点个数 <= 5000

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        # 首先判断是输入是否合法
        if not preorder or not inorder or set(preorder) != set(inorder) or len(preorder) != len(inorder):
            return None

        root = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:index+1], inorder[:index])
        root.right = self.buildTree(preorder[index+1:], inorder[index+1:])

        return root

