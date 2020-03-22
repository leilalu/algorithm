"""
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head):
        """"
            遍历链表，将链表转化为数组，利用双指针进行判断
            时间复杂度是O(n)
            空间复杂度也是O(n)

        """
        if not head:
            return True

        array = []
        pNode = head
        while pNode:
            array.append(pNode.val)
            pNode = pNode.next

        # 或者直接利用python的反向数组副本
        # return array == array[::-1]

        left = 0
        right = len(array) - 1
        while left < right:
            if array[left] != array[right]:
                return False
            left += 1
            right -= 1
        return True


class Solution2:
    def isPalindrome(self, head):
        """"
        我们可以将链表的后半部分反转（修改链表结构），然后将前半部分和后半部分进行比较。
        比较完成后我们应该将链表恢复原样。虽然不需要恢复也能通过测试用例，因为使用该函数的人不希望链表结构被更改。

        """

        if not head:
            return True
        # 使用快慢指针，一个一次走一步，一个一次走两步，当快指针到达链表尾部时，慢指针走到链表中间
        slow = fast = head
        while fast.next:
            slow = slow.next
            fast = fast.next
            if fast.next:
                fast = fast.next

        # 此时slow指向链表的后半部分开始的地方，fast指针在最后一位
        back = self.reverseList(slow)

        # 同时遍历两个链表
        pBack = back
        pFront = head
        while pBack:
            if pBack.val != pFront.val:
                return False
            pBack = pBack.next
            pFront = pFront.next

        return True

    def reverseList(self, head):
        pNode = head
        preNode = None

        while pNode:
            pNext = pNode.next
            pNode.next = preNode
            preNode = pNode
            pNode = pNext

        return preNode





