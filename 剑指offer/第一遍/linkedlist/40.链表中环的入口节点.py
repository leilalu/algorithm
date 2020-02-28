"""
题目描述
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    本题的重点是要把【找链表中环的入口结点】问题分解成三个子问题：
            1、判断一个链表中是否有环：
                方法：利用快慢双指针：如果走得快的指针追上了走得慢的指针，则说明链表中有环，并且相遇的结点一定在环中
                                   如果走的快的指针走到了链表的末尾，fast.next = None，则说明链表中没环，返回None
            2、确定链表中环中结点的个数：
                方法：如果链表中有环，那么快慢指针相遇的结点就是环中结点，从该节点出发，再回到该节点时，经过的就是环中所有的结点，可以计数
            3、确定链表中的入口节点：
                方法：重新设置快慢双指针：让走得快的指针先走【环中结点数】步，然后让两个指针一起走，当两个指针相遇时，就是环的入口

    """
    def MeetingNode(self, pHead):
        """
            判断链表中是否有环，如果有的话，返回某个环中结点
        """
        if not pHead:
            return

        slow = pHead.next
        # 只有一个节点 不含环
        if not slow:
            return

        fast = slow.next
        while fast and slow:
            if fast == slow:
                return fast

            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
        return None

    def EntryNodeOfLoop(self, pHead):
        """
            找出链表中环的入口结点
        """
        meetingNode = self.MeetingNode(pHead)

        # 如果不含环
        if not meetingNode:
            return None

        # 得到环中结点数目
        count = 1
        pNode = meetingNode
        while pNode.next != meetingNode:
            pNode = pNode.next
            count += 1

        # 先移动pNode1，次数为环中结点的数目
        pNode1 = pHead
        for i in range(count):
            pNode1 = pNode1.next

        # 再移动pNode1和pNode2，直到两者相遇
        pNode2 = pHead
        while pNode1 != pNode2:
            pNode1 = pNode1.next
            pNode2 = pNode2.next

        return pNode1

