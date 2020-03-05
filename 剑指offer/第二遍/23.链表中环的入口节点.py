class Solution:
    def MeetingNode(self, pHead):
        if not pHead:
            return None

        slow = pHead.next
        fast = slow.next
        while slow and fast:
            if slow == fast:
                return fast
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
        return None

    def FindEntry(self, pHead):
        meetNode = self.MeetingNode(pHead)
        if not meetNode:
            return None
        count = 1
        pNode = meetNode.next
        while pNode.next != meetNode:
            count += 1
            pNode = pNode.next

        pNode1 = pNode2 = pHead

        for i in range(count):
            pNode1 = pNode1.next

        while pNode1 != pNode2:
            pNode1 = pNode1.next
            pNode2 = pNode2.next

        return pNode1



