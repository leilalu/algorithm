class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def removeNthFromEnd(head, n):
    count = 0

    # 添加哑结点，可以用来简化极端情况，如链表中只有一个元素
    k = ListNode(0)
    k.next = head

    p = head

    while p:
        count += 1
        p = p.next

    index = count - n

    p = k

    while index > 0:
        p = p.next
        index -= 1

    p.next = p.next.next

    return k.next


def removeNthFromEnd_1(head, n):

    res = ListNode(0)
    res.next = head

    first = res
    second = res

    while n+1 > 0:
        first = first.next
        n -= 1

    while first:
        first = first.next
        second = second.next

    second.next = second.next.next

    return res.next



p = ListNode(0)
l1 = p
l1.next = ListNode(1)
l1 = l1.next
l1.next = ListNode(2)
l1 = l1.next
l1.next = ListNode(3)
l1 = l1.next
l1.next = ListNode(4)
l1 = l1.next
l1.next = ListNode(5)

res = removeNthFromEnd_1(p.next, 2)
while res:
    print(res.val)
    res = res.next
