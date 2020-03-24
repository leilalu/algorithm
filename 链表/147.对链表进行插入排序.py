"""
插入排序算法：

插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
重复直到所有输入数据插入完为止。

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1:
    def insertionSortList(self, head):
        if not head:
            return None
        pre = ListNode(0)
        preNode = pre
        cur = head
        while cur:
            pNext = cur.next
            while preNode.next and preNode.next.val < cur.val:
                preNode = preNode.next
            # 插入
            cur.next = preNode.next
            preNode.next = cur
            # 让pre回去
            preNode = pre
            cur = pNext
        return pre.next


class Solution2:
    def insertionSortList(self, head):
        # 开始尾部必须是负无穷大，任何数都比他大，才能链在它后面
        pre = ListNode(float('-inf'))
        preNode = pre
        tail = pre

        cur = head
        while cur:
            # 当当前结点比尾结点大时，直接连在后面
            if tail.val < cur.val:
                tail.next = cur
                tail = cur
                cur = cur.next
            else:
                pNext = cur.next
                # 可以控制尾结点最终为None，否则不能结束
                tail.next = pNext

                while preNode.next and preNode.next.val < cur.val:
                    preNode = preNode.next

                # 插入
                cur.next = preNode.next
                preNode.next = cur
                preNode = pre
                cur = pNext

        return pre.next

