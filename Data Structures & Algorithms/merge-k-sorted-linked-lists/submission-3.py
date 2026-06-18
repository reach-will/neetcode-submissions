# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        node = dummy
        heap_lists = [(node.val, i, node) for i, node in enumerate(lists)]
        heapq.heapify(heap_lists)
        while heap_lists:
            _, i, node.next = heapq.heappop(heap_lists)
            node = node.next
            if node.next:
                heapq.heappush(heap_lists, (node.next.val, i, node.next))
        return dummy.next
        