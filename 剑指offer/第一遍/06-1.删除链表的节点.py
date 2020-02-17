"""
题目一：在O(1)时间内删除链表结点

给定单向链表的头指针和一个节点指针，定义一个函数在O(1)时间内删除该节点。

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __del__(self):
        self.val = None
        self.next = None


class Solution1:
    def DeleteNode(self, head, node):
        """
            删除链表中指定结点的常规方法：
                要分三种情况讨论：
                    1、要删除的结点是头结点 pHead = pHead.next
                    2、要删除的结点是中间结点： 遍历链表到该结点，将该节点前一个结点的下一个节点指针指向该节点的下一个节点
                    3、要删除的是尾结点：遍历到链表的最后一个节点，将该节点的前一个结点的下一个节点指针指向None

            这种方法需要遍历链表，时间复杂度是O(n) 不符合本题要求

        :param head:
        :param node:
        :return:
        """

        # 检查无效输入
        if not head or not node:
            return []

        if head == node:
            # 删除头结点
            if node.next:
                # 当前链表有多个结点
                head = head.next
                node.__del__()
            else:
                # 链表只有一个结点
                node.__del__()
                head.__del__()

        else:
            # 删除中间结点或尾结点
            pNode = head
            while pNode.next != node:
                pNode = pNode.next
            pNode.next = node.next
            node.__del__()

        return self.printLinkedList(head)

    # 打印链表
    def printLinkedList(self, pHead):
        if not pHead:
            return []

        res = []
        pNode = pHead
        while pNode:
            res.append(pNode.val)
            pNode = pNode.next
        return res


class Solution2:
    def DeleteNode(self, head, node):
        """
            本题的重点在于【时间复杂度要求O(1)】,删除单向链表某个结点的常规做法是，从链表的头结点开始，按顺序遍历查找要删除的结点，并在链表
            中删除该结点，其时间复杂度是O(n)。
            如果要达到要求的时间复杂度O(1)，那一定不能在进行遍历操作
            注意到本题不是给定一个数值，删除该数值的结点，而是给出了要删除的结点，就包含要删除结点的下一个节点。
            现在知道了要删除结点，也知道了要删除结点的下一个结点，需要要删除结点的上一个结点，这是未知的。
            我们不知道要删除结点的上个节点，但是我们知道要删除结点的下个结点的上个节点，因此可以考虑把要删除的结点的下个节点删掉。
            那我们可以让把下一个结点的值复制给要删除的结点，然后把下一个节点删除

            要删除的结点应该分情况讨论，
                            1）如果要删除的是头结点 即 head == node 那么要把node和head全都delete
                            2）如果删除的是中间结点，则按上述方法
                            2）如果要删除的是尾结点，也就是说要删除的结点没有下一个节点，就无法使用上述方法，需要从头遍历链表

            时间复杂度分析：
                对于n-1个非尾结点来说，我们可以在O(1)的时间内把下一个结点的内存复制覆盖要删除的结点，并删除下一个节点
                对于尾结点来说，由于仍然需要顺序查找，时间复杂度是O(n)
                总的平均时间复杂度是 O[(n-1) * O(1) + O(n) * 1] / n 结果还是 O(1)

            【注意】当删除的结点的确在链表中时，才能够实现O(1),
                   如果不能确定结点是否在链表中，则需要O(n)的时间来判断链表中是否包含某一结点

        :param head:
        :param node:
        :return:
        """
        # 检查无效输入
        if not head or not node:
            return []

        # 要删除的结点不是尾结点
        if node.next:
            next = node.next
            node.val = next.val
            node.next = next.next
            next.__del__()

        # 链表只有一个节点，要删除的结点是头结点（也是尾结点）
        elif head == node:
            node.__del__()
            head.__del__()

        # 链表有多个节点，要删除的是尾结点
        else:
            pNode = head
            while pNode.next != node:
                pNode = pNode.next

            pNode.next = None
            node.__del__()

        return self.printLinkedList(head)

    # 打印链表
    def printLinkedList(self, pHead):
        if not pHead:
            return []
        res = []
        pNode = pHead
        while pNode:
            res.append(pNode.val)
            pNode = pNode.next
        return res


if __name__ == '__main__':
    node1 = ListNode(10)
    node2 = ListNode(11)
    node3 = ListNode(13)
    node4 = ListNode(15)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    s = Solution1()
    print(s.printLinkedList(node1))
    res = s.DeleteNode(node1, node1)
    print(res)





