"""

输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

 

示例 1：

输入：head = [1,3,2]
输出：[2,3,1]
 

限制：

0 <= 链表长度 <= 10000

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head):
        if not head:
            return []

        pNode = head
        stack = []

        while pNode:
            stack.append(pNode.val)
            pNode = pNode.next
        res = []
        while stack:
            res.append(stack.pop())

        return res