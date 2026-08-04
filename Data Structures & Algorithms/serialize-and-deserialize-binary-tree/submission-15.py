# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        queue = deque([root])
        serial = []
        while queue:
            node = queue.popleft()
            if not node:
                serial.append("")
                continue
            serial.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        return ",".join(map(str, serial)).rstrip(",")

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        serial = data.split(",")
        root = TreeNode(int(serial[0]))
        queue = deque([root])
        it = islice(serial, 1, None)
        for left in it:
            node = queue.popleft()
            if left:
                node.left = TreeNode(int(left))
                queue.append(node.left)
            right = next(it, "")
            if right:
                node.right = TreeNode(int(right))
                queue.append(node.right)
        return root
