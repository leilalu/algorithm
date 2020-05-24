"""
输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。

 

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]

"""


class Solution:
    def pathSum(self, root, sum):
        if not root:
            return []

        res = []
        stack = [(root, [root.val])]

        while stack:
            node, path = stack.pop()
            # 如果是叶节点，则计算路径和
            if not node.left and not node.right and self.getSum(path) == sum:
                res.append(path)

            if node.right:
                stack.append((node.right, path+[node.right.val]))

            if node.left:
                stack.append((node.left, path+[node.left.val]))

        return res


    def getSum(self, path):
        sumValue = 0
        for num in path:
            sumValue += num

        return sumValue
