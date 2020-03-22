"""
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL

"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     def reverseBetween(self, head: ListNode, m, n):
#         # first.next = second.next
#         #