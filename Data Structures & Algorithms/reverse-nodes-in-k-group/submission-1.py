# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        prev_group_tail = dummy
        curr_group_head = head
        while curr_group_head:
            prev = None
            curr_group_tail = curr_group_head
            for _ in range(k):
                if not curr_group_head:
                    curr = prev
                    prev = None
                    while curr:
                        temp = curr.next
                        curr.next = prev
                        prev = curr
                        curr = temp
                    break
                temp = curr_group_head.next
                curr_group_head.next = prev
                prev = curr_group_head
                curr_group_head = temp
            prev_group_tail.next = prev
            prev_group_tail = curr_group_tail
        return dummy.next