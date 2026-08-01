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
        q = deque([root])
        serial = []
        while q:
            n = len(q)
            for _ in range(n):
                top = q.popleft()
                if not top:
                    serial.append("")
                    continue
                serial.append(top.val)
                q.append(top.left)
                q.append(top.right)
            if all(x is None for x in q):
                break
        return ",".join(map(str, serial))

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        serial = data.split(",")
        root = TreeNode(int(serial[0]))
        queue = deque([root])
        for left, right in zip(serial[1::2], serial[2::2]):
            node = queue.popleft()
            if left:
                node.left = TreeNode(int(left))
                queue.append(node.left)
            if right:
                node.right = TreeNode(int(right))
                queue.append(node.right)
        return root
