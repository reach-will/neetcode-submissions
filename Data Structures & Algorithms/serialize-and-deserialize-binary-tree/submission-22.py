# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
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
        return ",".join(map(str, serial))

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
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

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))