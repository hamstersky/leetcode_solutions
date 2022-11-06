from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def listApproach(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    cur = head
    list = []

    while cur.next != None:
        list.append(cur)
        cur = cur.next

    list.append(cur)
    n = len(list) - n - 1

    if n == -1:
        head = head.next
    else:
        list[n].next = list[n].next.next

    return head


e = ListNode(5, None)
d = ListNode(4, e)
c = ListNode(3, d)
b = ListNode(2, c)
a = ListNode(1, b)

listApproach(a, 2)
