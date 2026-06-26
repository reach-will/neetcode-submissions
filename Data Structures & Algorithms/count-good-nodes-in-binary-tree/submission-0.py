# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root: TreeNode, pathMax: int) -> int:
        if not root:
            return 0
        if root.val >= pathMax:
            return self.dfs(root.left, root.val) + self.dfs(root.right, root.val) + 1
        return self.dfs(root.left, pathMax) + self.dfs(root.right, pathMax)
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root.left, root.val) + self.dfs(root.right, root.val) + 1