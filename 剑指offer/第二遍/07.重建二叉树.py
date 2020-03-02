"""
题目：
输入某二叉树的前序遍历和中序遍历的结果，请重建二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如，输入前序遍历序列[1,2,4,7,3,5,6,8]和中序遍历序列[4,7,2,1,5,3,8,6]

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def ConstructTree(pre, tin):
    if not pre or not tin or len(tin) != len(pre):
        return None
    if set(pre) != set(tin):
        return None

    root = pre[0]
    index = tin.index(root)

    root.left = ConstructTree(pre[1:index+1], tin[:index])
    root.right = ConstructTree(pre[index+1:], tin[index+1:])

    return root

