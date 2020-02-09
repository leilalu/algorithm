"""
题目描述
输入一个链表，按链表从尾到头的顺序返回一个ArrayList。

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # Brute force
    def printListFromTailToHead_1(self, listNode):
        """

            暴力法，遍历链表的结点，把每个结点的元素值保存在一个list中，再按逆序返回该list
            Note：python中逆序list可以通过列表切片完成list[::-1] 表示从头到尾，步长为-1

        :param listNode: 头结点
        :return: 按链表从尾到头的顺序返回的数组

        """
        res = []

        while listNode:
            res.append(listNode.val)
            listNode = listNode.next

        res = res[::-1]

        return res

    # 栈
    def printListFromTailToHead_2(self, listNode):
        """
            看到【从尾到头】想到使用栈，用两个数组实现一个栈。
            遍历链表的结点，每读取一个结点，就将该结点的元素值压入栈中，当链表遍历结束后，从栈中取出一个元素输出
            【注意】使用堆栈时不要忘记使用栈的基本操作:pop push 等

        :param listNode: 链表头结点
        :return: 按链表从尾到头的顺序返回的数组

        """

        stack = []
        res = []
        while listNode:
            stack.append(listNode.val)
            listNode = listNode.next

        while stack:
            res.append(stack.pop())

        return res

    # 递归
    def printListFromTailToHead_3(self, listNode):
        """
            可以用【栈】，自然可以想到使用【递归】
            每访问到一个节点的时候，先递归输出它后面的结点，再输出该节点自身，这样链表的输出结果就反过来了

            【缺点】当链表非常长时，使用递归会导致函数调用的层级很深，导致函数调用栈溢出，鲁棒性没有使用栈好


        :param listNode:
        :return:
        """

        if listNode:
            if listNode.next:
                self.printListFromTailToHead_3(listNode.next)
            print(listNode.val)


if __name__ == '__main__':
    listNode = ListNode(1)
    listNode_1 = ListNode(2)
    listNode_2 = ListNode(3)
    listNode_3 = ListNode(4)
    listNode.next = listNode_1
    listNode_1.next = listNode_2
    listNode_2.next = listNode_3
    s = Solution()
    res = s.printListFromTailToHead_3(listNode)
    print(res)
