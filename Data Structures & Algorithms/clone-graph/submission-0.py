"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def clone_node(self, node: Optional['Node']) -> Optional['Node']:
        if node in self.original_to_clone:
            return

        cloned_node = Node(node.val)
        self.original_to_clone[node] = cloned_node

        for neighbor in node.neighbors:
            self.clone_node(neighbor)
            cloned_node.neighbors.append(self.original_to_clone[neighbor])

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        self.original_to_clone = {None: None}
        self.clone_node(node)
        return self.original_to_clone[node]
