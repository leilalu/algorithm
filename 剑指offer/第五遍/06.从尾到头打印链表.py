"""
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

示例 1：

输入：head = [1,3,2]
输出：[2,3,1]

"""

"""
法一：
看到题干中的【从尾到头】【反向】【从后向前】都要想到使用【栈】来实现反向操作
先从头到尾遍历链表，将每个链表的节点值入栈，然后按顺序弹栈，加入到返回列表中。
相当于遍历了两遍链表，时间复杂度是O(n)，使用了额外的栈来保存节点的值，空间复杂度是O(n)


法二：
可以用栈，就可以用【递归】，递归也可以从后往前计算
但是递归也需要空间，空间复杂度仍然是O(n)，遍历了所有的节点，时间复杂度也是O(n)


"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head):
        # 首先判断输入是否合法
        if not head:
            return []
        # 使用栈保存结点值
        stack = []
        pNode = head
        while pNode:
            stack.append(pNode.val)
            pNode = pNode.next

        res = []
        while stack:
            res.append(stack.pop())

        return res

    def reversePrint1(self, head):
        res = []

        def PrintListNode(listNode):
            if listNode:
                PrintListNode(listNode.next)
                res.append(listNode.val)

        PrintListNode(head)

        return res



