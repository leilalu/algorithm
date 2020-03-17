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


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __del__(self):
        self.val = None
        self.next = None


class Solution1:
    def deleteNode(self, head, val):
        """"
            输入的是要删除结点的值
        """
        if not head:
            return None

        # 不要忘记删除的有可能是头结点！！！！因此要在前面再加上一个节点！！！
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


class Solution2:
    def deleteNode(self, head, node):
        """"
            输入的是要删除结点的指针
        """
        if not head or not node:
            return []

        if node.next:
            # 如果不是尾结点
            pNext = node.next
            node.val = pNext.val
            node.next = pNext.next
            pNext.__del__()

        # 如果只有一个结点
        elif head == node:
            head.__del__()
            node.__del__()
        # 如果不止一个节点，删除尾结点，需要遍历
        else:
            pNode = head
            while pNode.next != node:
                pNode = pNode.next

            pNode.next = None
            node.__del__()

        return head























