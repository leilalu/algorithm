"""
题目二：删除链表中重复的节点

在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __del__(self):
        self.val = None
        self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        """
            由于链表已经排序，因此重复结点是相邻的
            需要充分分类讨论：
                1、当pHead为空 或者 只有一个节点 pHead.next == None 时，不存在重复的结点 返回
                2、当有多个节点时，重复的结点可以分为三类：
                        1、头结点重复 由于头结点可能被删除，因此需要在头结点前再加一个结点
                        2、中间结点重复
                        3、尾结点重复
                3、链表没有重复
                4、链表中所有结点都是重复的

        :param pHead:
        :return:
        """
        # 检查无效输入
        if not pHead:
            return

        if not pHead.next:
            return pHead

        pre = ListNode(0)
        pre.next = pHead
        pNode = pHead
        preNode = pre

        while pNode:
            if pNode.next and pNode.val == pNode.next.val:
                while pNode.next and pNode.val == pNode.next.val:
                    pNode = pNode.next
                preNode.next = pNode.next
                pNode = pNode.next

            else:
                preNode = preNode.next
                pNode = pNode.next

        return self.printLinkedList(pre.next)

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
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(3)
    node5 = ListNode(4)
    node6 = ListNode(4)
    node7 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    s = Solution()
    print(s.printLinkedList(node3))
    res = s.deleteDuplication(node3)
    print(res)



