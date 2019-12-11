"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1: ListNode, l2: ListNode):
    """

    :param l1:
    :param l2:
    :return:

    方案描述：先分别计算两个链表的长度并进行比较，以长的那个个数为外层循环，首先判断上次循环进位，然后分别将两个链表对应的元素相加，并加上进位数，
            如果本次循环仍然大于10，则进位数为十位，直到短的列表没有下一位，长的列表落下来。最高位如果进位，还要再添一位。

    """
    result = ListNode(0)  # 作为根节点的引用
    p = result

    circle = 0  # 作为上一次相加是否需要进1的依据

    # l1 和 l2指的都是当前链表的节点，包括其value和next，while l1 and l2指的是当前l1和l2均有节点
    while l1 and l2:
        # 创建节点
        p.next = ListNode((l1.val + l2.val + circle) % 10)
        # 进位
        circle = (l1.val + l2.val + circle) // 10

        p, l1, l2 = p.next, l1.next, l2.next

    # 此时l1和l2中至少有一个没有节点了，或者两个都没有节点了
    # l1 = l1 if l1 else l2
    if l1:
        l1 = l1
    else:
        l1 = l2
    # 此时 l1是两个链表中还有节点的那个，或者已经没有节点了
    # 判断当前是否有进位
    while circle:
        if l1:
            p.next = ListNode((l1.val + circle) % 10)
            circle = (l1.val + circle) // 10
            p, l1 = p.next, l1.next
        else:
            p.next = ListNode(circle)
            p = p.next
            break

    # 此时l1已经空了，为None，而p.next不可以没有值，否则会报错，因此一定要加上这句
    p.next = l1

    return result.next


"""

今日收获：
1、链表的基本操作：链表由节点构成，每个节点由一个值和下一个节点构成，因此在创建一个链表时可以先创建一个ListNode(0)，一个值为0的节点，
                不用担心这个节点使链表的头节点冗余，我们可以返回该节点.next
                
2、在计算两数的加减乘除时前往不要忘记进位，进位进十位，十位应该有【//】获得，保留个位，应该通过取余数【%】或是取模得到

3、判断链表的节点是否存在（是否为None）可以直接判断，如：if l1

4、python的三元表达式：var = 1 if 条件成立 else 2 的意思是 if 条件成立： var=1 else： var = 2

5、链表结束时一定要让其next为None，否则将会报错

                
"""






