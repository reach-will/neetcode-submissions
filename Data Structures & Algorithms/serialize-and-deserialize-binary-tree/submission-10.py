from collections import deque
from typing import Optional

class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "null"
        
        result = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("null")
        return ",".join(result)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        if vals[0] == "null":
            return None
        
        root = TreeNode(int(vals[0]))
        queue = deque([root])
        i = 1
        while queue:
            node = queue.popleft()
            # left child
            if vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            # right child
            if vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
        return root