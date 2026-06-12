class Node:
    def __init__(self, key, val, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.node_cache = {}
        
        self.left = Node(0, 0)
        self.right = Node(0, 0, prev = self.left)
        self.left.next = self.right

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert_node(self, node):
        node.prev = self.right.prev
        node.next = self.right
        self.right.prev.next = node
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.node_cache:
            return -1
        self.remove_node(self.node_cache[key])
        self.insert_node(self.node_cache[key])
        return self.node_cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.node_cache:
            self.node_cache[key].val = value
            self.remove_node(self.node_cache[key])
            self.insert_node(self.node_cache[key])
            return

        self.node_cache[key] = Node(key, value)
        self.insert_node(self.node_cache[key])

        if len(self.node_cache) > self.capacity:
            lru_node = self.left.next
            self.remove_node(lru_node)
            del self.node_cache[lru_node.key]
