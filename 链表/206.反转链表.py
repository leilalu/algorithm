"""
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1:
    def reverseList(self, head):
        """"
            迭代法

            时间复杂度 O(N)
            空间复杂度 O(1)

        """
        if not head:
            return None

        pNode = head
        preNode = None

        while pNode:
            pNext = pNode.next

            pNode.next = preNode
            preNode = pNode
            pNode = pNext

        return preNode


class Solution2:
    def reverseList(self, head):
        """"
            递归法
            时间复杂度：O(n)，假设 n 是列表的长度，那么时间复杂度为 O(n)。
            空间复杂度：O(n)，由于使用递归，将会使用隐式栈空间。递归深度可能会达到 n 层。

            执行reverseList(5),head节点为5处,返回5->null;
            执行reverseList(4),head节点为4,从4节点的指针为4->5->null,执行head.next.next = head; head.next = null;后p节点的结果为5->4->null;
            执行reverseList(3),head节点为3,从3节点的指针为3->4->null,[注意reverseList(4)只是改变了4和4节点后的地址互换，其之前的指针指向地址未变],执行head.next.next = head;head.next = null;后p节点的结果为5->4->3->null;
            执行reverseList(2),head节点为2,从2节点的指针为2->3->null,执行head.next.next = head;head.next = null;后p节点的结果为5->4->3->2->null;
            执行reverseList(1),head节点为1,从1节点的指针为1->2->null,执行head.next.next = head;head.next = null;后p节点的结果为5->4->3->2->1->null; 递归结束

        """
        # 递归出口，当到达最后一个结点时，反向
        if not head or not head.next:
            return head
        # 先将当前结点的后续结点反向
        p = self.reverseList(head.next)
        # 将当前结点链在后续结点后面，后续结点 head.next 后续结点的后面 head.next.next
        head.next.next = head

        # 现在，当前结点head是一个尾结点了，他的next要为None
        head.next = None

        # 返回头指针
        return p



