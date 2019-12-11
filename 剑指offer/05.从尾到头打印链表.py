"""
题目描述
输入一个链表，按链表从尾到头的顺序返回一个ArrayList。

"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead_1(self, listNode):
        """
        暴力法，先把一个链表存在一个list中，再按逆序返回


        Note：python中逆序list可以通过列表切片完成list[::-1] 表示从头到尾，步长为-1

        :param listNode:
        :return:
        """
        array = []
        while listNode:
            array.append(listNode.val)
            listNode = listNode.next

        array_new = array[::-1]

        return array_new

    def printListFromTailToHead_2(self, listNode):
        """
        看到【返回逆序/从尾到头】等关键词要想到使用数据结构【栈】
        栈是天然的逆序

        :param listNode:
        :return:
        """
        stack = []
        while listNode:
            stack.append(listNode.val)
            listNode = listNode.next

        result = []
        while stack:
            temp = stack.pop()
            result.append(temp)
        return result


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)

    node1.next = node2
    node2.next = node3

    s = Solution()
    res = s.printListFromTailToHead_2(node1)
    print(res)