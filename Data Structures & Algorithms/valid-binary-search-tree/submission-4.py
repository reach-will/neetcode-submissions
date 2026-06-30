# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfsInner(self, root: Optional[TreeNode], left: int, right: int) -> bool:
        if not root:
            return True
        if root.val <= left or root.val >= right:
            return False
        return self.dfsInner(root.left, left = left, right = root.val) and self.dfsInner(root.right, left = root.val, right = right)

    def dfsLeft(self, root: Optional[TreeNode], right: int) -> bool:
        if not root:
            return True
        if root.val >= right:
            return False
        return self.dfsLeft(root.left, right = root.val) and self.dfsInner(root.right, left = root.val, right = right)

    def dfsRight(self, root: Optional[TreeNode], left: int) -> bool:
        if not root:
            return True
        if root.val <= left:
            return False
        return self.dfsInner(root.left, left = left, right = root.val) and self.dfsRight(root.right, left = root.val)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfsLeft(root.left, right = root.val) and self.dfsRight(root.right, left = root.val)
