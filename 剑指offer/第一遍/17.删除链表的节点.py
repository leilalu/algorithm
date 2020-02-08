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


class Solution:
    def DeleteNode(self, head, node):
        if not head or not node:
            return
        # 要删除的结点不是尾结点
        if node.next:
            next = node.next
            node.val = next.val
            node.next = next.next
            next.__del__()

        # 链表只有一个节点，删除头结点（也是尾结点）
        elif head == node:
            node.__del__()
            head.__del__()
        # 链表有多个节点，删除尾结点
        else:
            pNode = head
            while pNode.next != node:
                pNode = pNode.next

            pNode.next = None
            node.__del__()


if __name__ == '__main__':
    node1 = ListNode(10)
    node2 = ListNode(11)
    node3 = ListNode(13)
    node4 = ListNode(15)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    s = Solution()
    res = s.DeleteNode(node1, node3)






