# 1.two pointers - iteratively 
# a typical sub-question of lots of other questions 
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def reverseList(head:ListNode)->Optional[ListNode]:
    prev , curr = None, head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

# recursive solution:
def reverseList(head:ListNode):
    if not head:
        return None

    newHead = head
    if head.next:
        newHead = self.reverseList(head.next)
        head.next.next = head
    head.next = None
    return newHead

# a better recursive solution
def reverseListRecursive(self, head):
    def reverse(cur, prev):
        if cur is None:
            return prev
        else:
            next = cur.next
            cur.next = prev
            return reverse(next, cur)

    return reverse(head, None)