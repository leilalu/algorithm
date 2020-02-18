"""
题目描述
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。
（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）

"""


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution1:
    def Clone(self, pHead):
        """
            重点优化【定位结点的random子结点】
                使用空间换时间的方法，分为两大步：
                    第一步复制原始链表上的每个节点N，创建N'，然后把这些创建出来的结点用next连接起来。并且把<N,N'>的配对信息放到一个哈希表中
                    第二步设置复制链表上的每个节点的random，如果原始链表中结点N的random指向结点S，那么在复制链表中对应的N'应该指向S'

            对于有n个节点的链表，需要一个大小为O(n)的哈希表
            时间复杂度为O(n)
            空间复杂度也是O(n)

        :param pHead:
        :return:
        """

        if not pHead:
            return

        # 从头到尾复制next结点
        # 用hash表存储每个原结点-和他的复制结点
        node_clone = {}
        pHead_clone = RandomListNode(pHead.label)  # 复制头结点
        node_clone[pHead] = pHead_clone


        pNode_clone = pHead_clone
        pNode = pHead.next
        while pNode:
            node = RandomListNode(pNode.label)
            pNode_clone.next = node
            pNode_clone = pNode_clone.next

            node_clone[pNode] = pNode_clone

            pNode = pNode.next

        # 设置random结点
        pNode = pHead_clone
        while pNode:
            node = [k for k, v in node_clone.items() if v == pNode]
            # 注意 一定要判断原链表结点的random是不是None
            if not node[0].random:
                pNode.random = None
            else:
                pNode.random = node_clone[node[0].random]
            pNode = pNode.next

        return pHead_clone

    def printLinkedList(self, pHead):
        if not pHead:
            return []

        res = []
        pNode = pHead
        while pNode:
            res.append(pNode.label)
            pNode = pNode.next

        return res


class Solution2:
    def Clone(self, pHead):
        """
        复制复杂链表可以分三步：
                1、第一步：复制原链表的结点，并将复制的结点链接在原结点后
                2、第二步：设置复制结点的random： 原链表的next 的 random = 原链表的random 的 next
                3、第三步：原链表和复制链表拆开，奇数结点是原链表，偶数结点是复制链表

        :param pHead:
        :return:
        """
        if not pHead:
            return
        self.Clone_element(pHead)
        self.SetRandom(pHead)
        return self.SplitLinkedList(pHead)

    def Clone_element(self, pHead):
        pNode = pHead
        while pNode:
            # 创建复制结点
            node = RandomListNode(pNode.label)
            # 插入复制结点
            node.next = pNode.next
            pNode.next = node
            # 指向下一个原结点
            pNode = node.next

    def SetRandom(self, pHead):
        pNode = pHead
        while pNode:
            clone = pNode.next
            if pNode.random is not None:
                clone.random = pNode.random.next

            pNode = clone.next

    def SplitLinkedList(self, pHead):
        pNode = pHead
        pClonedHead = pClonedNode = pNode.next
        pNode.next = pClonedHead.next
        pNode = pNode.next

        while pNode:
            pClonedNode.next = pNode.next
            pClonedNode = pClonedNode.next
            pNode.next = pClonedNode.next
            pNode = pNode.next

        return pClonedHead


if __name__ == '__main__':
    A = RandomListNode('A')
    B = RandomListNode('B')
    C = RandomListNode('C')
    D = RandomListNode('D')
    E = RandomListNode('E')

    A.next = B
    A.random = C

    B.next = C
    B.random = E

    C.next = D

    D.next = E
    D.random = B

    s = Solution2()
    res = s.Clone(A)
    print(res)








