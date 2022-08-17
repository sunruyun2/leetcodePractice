# dumb me
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # dummy = ListNode(101)
        # dummy.next = head
        # curr, prev = dummy, dummy.next

        # while prev:
        #     while prev and curr.val == prev.val:
        #         prev = prev.next
        #     curr.next = prev
        #     if prev:
        #         curr = curr.next
        #         prev = prev.next
        curr = head
        while curr:
            while curr.next and curr.next.val == curr.val:
                curr.next = curr.next.next
            curr = curr.next
            
        return head


