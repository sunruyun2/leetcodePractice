#1. very intuitive and try to catch a lot of exception manually
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElement(self, head:ListNode , val)->ListNode:
        while head is not None and head.val == val:
            head = head.next

        if not head:
            return None

        prev = head

        while prev and prev.next:
            while prev.next is not None and prev.next.val == val:
                prev.next = prev.next.next
            prev = prev.next
        return head


# 2. two pointers and use dummy node to catch edge cases

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElement(self, head:ListNode , val)->ListNode:
        dummy = ListNode()
        dummy.next = head

        prev = dummy
        curr = prev.next
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next

        return dummy.next