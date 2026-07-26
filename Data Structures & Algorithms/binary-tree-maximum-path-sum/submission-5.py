# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def continuousSum(self, root: Optional[TreeNode]) -> int:
        if not root.left:
            if not root.right:
                self.res = max(self.res, root.val)
                return root.val

            right = self.continuousSum(root.right)
            continuous = root.val + max(0, right)
            self.res = max(self.res, continuous)
            return continuous

        if not root.right:
            left = self.continuousSum(root.left)
            continuous = root.val + max(0, left)
            self.res = max(self.res, continuous)
            return continuous

        left = self.continuousSum(root.left)
        right = self.continuousSum(root.right)
        continuous = root.val + max(0, left, right)
        self.res = max(self.res, continuous, left + right + root.val)
        return continuous

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val
        self.continuousSum(root)
        return self.res
