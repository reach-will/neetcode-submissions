# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    count = 0
    res = -1
    def dfs(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        if self.count == 0:
            return
        self.dfs(root.left)
        self.count -= 1
        if self.count == 0:
            self.res = root.val
            return
        self.dfs(root.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = k
        self.dfs(root)
        return self.res