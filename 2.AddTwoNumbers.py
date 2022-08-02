# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution
# pay attention to edge case: 1. carry 2. the length of list 3.Nonetype
def addTwoNumbers(l1:ListNode , l2: ListNode) ->ListNode:
    dummy = ListNode()
    curr = dummy
    carry = 0

    while l1 or l2 or carry:
        l1Val = l1.val if l1 else 0
        l2Val = l2.val if l2 else 0
        sum = l1.val + l2.val + carry
        carry = sum // 10
        curr.next = ListNode(sum % 10)
        curr = curr.next
        l1 = l1.next
        l2 = l2.next

    return dummy.next
