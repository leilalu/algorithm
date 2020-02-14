"""
题目描述
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。
（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）

"""


class ComplexListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.random = None


class Solution1:
    def Clone(self, pHead):
        """
            重点优化【定位结点的pSibling子结点】
                使用空间换时间的方法，分为两大步：
                    第一步复制原始链表上的每个节点N，创建N'，然后把这些创建出来的结点用next连接起来。并且把<N,N'>的配对信息放到一个哈希表中
                    第二步设置复制链表上的每个节点的random，如果原始链表中结点N的random指向结点S，那么在复制链表中对应的N'应该指向S'

            对于有n个节点的链表，需要一个大小为O(n)的哈希表
            时间复杂度为O(n)
            空间复杂度也是O(n)

        :param pHead:
        :return:
        """

        # 检查输入是否合法
        if not pHead:
            return

        hashdict = {}

        pNode = pHead
        temp = ComplexListNode(0)
        pNode_clone = ComplexListNode(pNode.val)
        temp.next = pNode_clone
        hashdict[pNode_clone] = pNode
        while pNode.next:
            pNode = pNode.next
            node = ComplexListNode(pNode.val)
            pNode_clone.next = node
            hashdict[pNode_clone] = pNode

        pHead_clone = temp.next
        pNode = pHead_clone
        while pNode:
            pSibling = hashdict[pNode].Sibling




