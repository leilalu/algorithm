"""
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:
输入: 4->2->1->3
输出: 1->2->3->4

示例 2:
输入: -1->5->3->4->0
输出: -1->0->3->4->5

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1:
    def sortList(self, head):
        """"
            链表的归并排序
            递归法
        """
        # 递归出口
        if not head or not head.next:
            return head

        # 利用快慢指针拆分链表
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        mid = slow.next
        slow.next = None

        # 递归进行拆分链表,并排序
        left = self.sortList(head)
        right = self.sortList(mid)

        # 合并有序链表
        merge = res = ListNode(0)
        while left and right:
            if left.val < right.val:
                merge.next = left
                left = left.next
            else:
                merge.next = right
                right = right.next
            merge = merge.next
        # 如果left 或者 right没有合并完
        if left:
            merge.next = left
        else:
            merge.next = right
        return res.next


class Solution2:
    def sortList(self, head):
        """"
            归并排序
            非递归法

            1、首先统计链表的长度length，用于通过判断intv < length 判定是否完成排序
            2、额外生命一个结点res，作为头部后面5接整个链表，用于
                1）intv *= 2 即切换到下一轮合并时，可以通过res.next 找到链表头部h
                2）执行排序合并时，需要一个辅助结点作为头部，而res则作为链表头部排序合并时的辅助头部pre，
                   后面的合并排序可以将上次合并排序的尾部tail用作辅助结点

        """
        pNode = head
        length = 0
        # 遍历链表，计算结点个数
        while pNode:
            length = length+1
            pNode = pNode.next
        res = ListNode(0)
        res.next = head  # 哑结点

        # 合并
        intv = 1
        while intv < length:
            pre = res
            pNode = res.next
            while pNode:
                h1 = pNode
                i = intv
                while i and pNode:
                    pNode = pNode.next
                    i -= 1
                if i:
                    break  # 如果h2为空，不需要合并

                h2 = pNode
                i = intv
                while i and pNode:
                    pNode = pNode.next
                    i -= 1

                c1 = intv
                c2 = intv-i

                # 合并h1和h2
                while c1 and c2:
                    if h1.val < h2.val:
                        pre.next = h1
                        h1 = h1.next
                        c1 -= 1
                    else:
                        pre.next = h2
                        h2 = h2.next
                        c2 -= 1

                    pre = pre.next

                if c1:
                    pre.next = h1
                else:
                    pre.next = h2

                while c1 > 0 or c2 > 0:
                    pre = pre.next
                    c1 -= 1
                    c2 -= 1
                pre.next = pNode
            intv *= 2
        return res.next
















