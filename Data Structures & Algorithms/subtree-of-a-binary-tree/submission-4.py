class Solution:
    def serialize(self, root: Optional[TreeNode]) -> str:
        parts = []
        def dfs(node):
            if not node:
                parts.append("#")
                return
            parts.append(f"${node.val}")
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return "".join(parts)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.serialize(subRoot) in self.serialize(root)