"""
题目：
给定一棵二叉树和其中的一个节点，如何找中序遍历序列的下一个结点？
树中的结点除了有两个分别指向左、右子结点的指针，还有一个指向父结点的指针。

"""


def FindNextNode(pHead, pNode):
    """"
        如果是根结点：如果有左结点，返回左结点
                    如果没有右结点，是否有父结点：
                        如果有父结点：
                            它是左子结点：返回父结点
                            它是右子结点：返回父结点的父结点，直到某个父结点是左子结点
        如果是左结点，返回父结点
        如果是
    """
    if not pHead or not pNode:
        return None

    pNext = None
    if pNode.right:
        right = pNode.right
        while right.left:
            right = right.left
        pNext = right

    elif pNode.next:
        parent = pNode.next
        current = pNode
        while parent and current == parent.right:
            current = parent
            parent = parent.next

        pNext = parent

    return pNext




