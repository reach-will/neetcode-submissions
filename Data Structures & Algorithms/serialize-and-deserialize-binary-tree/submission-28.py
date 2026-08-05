# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Codec:
    NULL = ""
    SEP = ","

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        vals = []
        self._serialize_dfs(root, vals)
        return self.SEP.join(vals)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = iter(data.split(self.SEP))
        return self._deserialize_dfs(vals)

    def _serialize_dfs(self, node: Optional[TreeNode], vals: list[str]) -> None:
        if node is None:
            vals.append(self.NULL)
            return

        vals.append(str(node.val))
        self._serialize_dfs(node.left, vals)
        self._serialize_dfs(node.right, vals)

    def _deserialize_dfs(self, vals) -> Optional[TreeNode]:
        val = next(vals)

        if val == self.NULL:
            return None

        node = TreeNode(int(val))
        node.left = self._deserialize_dfs(vals)
        node.right = self._deserialize_dfs(vals)
        return node
