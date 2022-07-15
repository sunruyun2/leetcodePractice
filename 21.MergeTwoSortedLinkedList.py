# hwo to solve a linked list question
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1:ListNode , list2:ListNode):
    dummy = ListNode()
    tail =  dummy

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    if list1:
        tail.next = list1
    if list2:
        tail.next = list2


    return dummy.next

Node1 = ListNode(1)
Node2 = ListNode(2)
Node3 = ListNode(4)
Node1.next = Node2
Node2.next = Node3

NodeTwo1 = ListNode(1)
NodeTwo2 = ListNode(3)
NodeTwo3 = ListNode(4)
NodeTwo1.next = NodeTwo2
NodeTwo2.next = Node3

print(mergeTwoLists(Node1,NodeTwo1).val)
