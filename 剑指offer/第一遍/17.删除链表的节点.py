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
        """
            本题的重点在于【时间复杂度要求O(1)】,删除单向链表某个结点的常规做法是，从链表的头结点开始，按顺序遍历查找要删除的结点，并在链表
            中删除该结点，其时间复杂度是O(n)。
            如果要达到要求的时间复杂度O(1)，那一定不能在进行遍历操作
            注意到本题不是给定一个数值，删除该数值的结点，而是给出了要删除的结点，就包含要删除结点的下一个节点。
            现在知道了要删除结点，也知道了要删除结点的下一个结点，需要要删除结点的上一个结点，这是未知的。
            那我们可以让把下一个结点的值复制给要删除的结点，然后把下一个节点删除

            但是需要分情况讨论，如果头结点就是要删除的结点 即 head == node 那么要把node和head全都delete
                             如果尾结点是要删除的结点，也就是说要删除的结点没有下一个节点，就无法使用上述方法，需要从头遍历链表

        :param head:
        :param node:
        :return:
        """
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
    print(res)





