# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        right = head

        for _ in range(n):
            right = right.next

        dummy = ListNode(0, head)
        left = dummy
        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next