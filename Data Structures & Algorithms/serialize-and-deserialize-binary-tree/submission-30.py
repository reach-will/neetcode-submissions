# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Codec:
    NULL_TOKEN = ""
    DELIMITER = ","

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        tokens = []
        self._serialize_dfs(root, tokens)
        return self.DELIMITER.join(tokens)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        token_ierator = iter(data.split(self.DELIMITER))
        return self._deserialize_dfs(token_ierator)

    def _serialize_dfs(self, node: Optional[TreeNode], tokens: list[str]) -> None:
        if node is None:
            tokens.append(self.NULL_TOKEN)
            return

        tokens.append(str(node.val))
        self._serialize_dfs(node.left, tokens)
        self._serialize_dfs(node.right, tokens)

    def _deserialize_dfs(self, token_ierator) -> Optional[TreeNode]:
        token = next(token_ierator)

        if token == self.NULL_TOKEN:
            return None

        node = TreeNode(int(token))
        node.left = self._deserialize_dfs(token_ierator)
        node.right = self._deserialize_dfs(token_ierator)
        return node
