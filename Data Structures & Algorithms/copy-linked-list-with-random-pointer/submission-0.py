"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_list = []
        node_to_index = {}
        node = head
        i = 0
        while node:
            node_list.append(node)
            node_to_index[node] = i
            i += 1
            node = node.next
        dummy = Node(0)
        prev = dummy
        node_copy_list = []
        for node in node_list:
            prev.next = Node(x=node.val)
            prev = prev.next
            node_copy_list.append(prev)
        for node, node_copy in zip(node_list, node_copy_list):
            if node.random:
                node_copy.random = node_copy_list[node_to_index[node.random]]
            else:
                node_copy.random = None
        return dummy.next