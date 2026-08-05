from typing import Optional


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    NULL = "#"
    SEP = ","

    def serialize(self, root: Optional[TreeNode]) -> str:
        tokens = []
        self._build_tokens(root, tokens)
        return self.SEP.join(tokens)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        tokens = data.split(self.SEP)
        return self._build_tree(tokens)

    def _build_tokens(self, node: Optional[TreeNode], tokens: list[str]) -> None:
        if node is None:
            tokens.append(self.NULL)
            return

        tokens.append(str(node.val))
        self._build_tokens(node.left, tokens)
        self._build_tokens(node.right, tokens)

    def _build_tree(self, tokens: list[str]) -> Optional[TreeNode]:
        value = tokens.pop(0)

        if value == self.NULL:
            return None

        node = TreeNode(int(value))
        node.left = self._build_tree(tokens)
        node.right = self._build_tree(tokens)
        return node