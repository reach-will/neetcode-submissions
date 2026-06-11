# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nxt = head
        prev = None

        while nxt:
            curr = nxt
            nxt = curr.next
            curr.next = prev
            prev = curr

        return prev
