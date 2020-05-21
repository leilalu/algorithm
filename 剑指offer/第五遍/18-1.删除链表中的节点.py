"""
给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。

返回删除后的链表的头节点。

注意：此题对比原题有改动

示例 1:

输入: head = [4,5,1,9], val = 5
输出: [4,1,9]
解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
示例 2:

输入: head = [4,5,1,9], val = 1
输出: [4,5,9]
解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.

"""
"""
根据要删除的节点的位置分类讨论：
如果删除的是尾节点（即链表长度大于1）则按顺序删除
如果删除的不是尾节点，那么
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __del__(self):
        self.x = None
        self.next = None


class Solution:
    def deleteNode(self, head, val):
        # 首先判断输入是否合法
        if not head:
            return None

        # 因为有可能删除头节点，因此添加辅助头指针
        preNode = ListNode(0)
        preNode.next = head
        pNode = preNode

        while pNode.next:
            if pNode.next.val == val:
                pNext = pNode.next
                pNode.next = pNext.next
                break
            else:
                pNode = pNode.next

        return preNode.next

    def deleteNode(self, head, node):
        """
        输入的是待删除的节点
        """
        if not head:
            return None

        # 如果不是尾节点
        if node.next:
            pNext = node.next
            node.val = pNext.val
            node.next = pNext.next
            pNext.__del__()
        # 如果是尾节点
        # 如果既是尾节点又是头节点，说明链表长度为1
        elif head == node:
            head.__del__()
            node.__del__()
        else:
            pNode = head
            while pNode.next != node:
                pNode = pNode.next
            pNode.next = None
            node.__del__()

        return head






