# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = l1
        carry = False

        while l1.next and l2.next:
            s = l1.val + l2.val + (1 if carry else 0)
            if s < 10:
                l1.val = s
                carry = False
            else:
                l1.val = s - 10
                carry = True
            l1 = l1.next
            l2 = l2.next

        if l2.next:
            l1.next = l2.next

        s = l1.val + l2.val + (1 if carry else 0)
        if s < 10:
            l1.val = s
            return head
        l1.val = s - 10

        if not l1.next:
            l1.next = ListNode(1)
            return head

        l1 = l1.next

        while l1.next:
            if l1.val != 9:
                l1.val = l1.val + 1
                return head
            l1.val = 0
            l1 = l1.next

        if l1.val != 9:
            l1.val = l1.val + 1
            return head
        l1.val = 0
        l1.next = ListNode(1)

        return head
