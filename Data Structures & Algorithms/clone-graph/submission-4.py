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
            return self.original_to_clone[node]

        cloned_node = Node(node.val)
        self.original_to_clone[node] = cloned_node

        for neighbor in node.neighbors:
            cloned_node.neighbors.append(self.clone_node(neighbor))
        return cloned_node

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        self.original_to_clone = {}
        return self.clone_node(node)
