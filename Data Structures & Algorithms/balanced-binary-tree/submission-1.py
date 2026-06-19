# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root: Optional[TreeNode]) -> tuple[bool, int]:
        if not root:
            return True, 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        return left[0] and right[0] and abs(right[1] - left[1]) <= 1, max(left[1], right[1]) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)[0]