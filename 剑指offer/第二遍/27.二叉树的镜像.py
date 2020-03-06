"""
题目描述
操作给定的二叉树，将其变换为源二叉树的镜像。

输入描述:
二叉树的镜像定义：
        源二叉树
    	    8
    	   /  \
    	  6   10
    	 / \  / \
    	5  7 9 11

    	镜像二叉树
    	    8
    	   /  \
    	  10   6
    	 / \  / \
    	11 9 7  5

"""


class Solution:
    def Mirror(self, root):
        if not root:
            return None

        if not root.left and not root.right:
            return

        temp = root.left
        root.left = root.right
        root.right = temp

        if root.left:
            self.Mirror(root.left)

        if root.right:
            self.Mirror(root.right)

