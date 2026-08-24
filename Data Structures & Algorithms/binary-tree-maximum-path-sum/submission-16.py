# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def continuousSum(root: Optional[TreeNode]) -> int:
            if not root:
                return 0

            nonlocal res
            left_max = continuousSum(root.left)
            right_max = continuousSum(root.right)
            continuous = root.val + max(0, left_max, right_max)
            res = max(res, continuous, left_max + right_max + root.val)
            return continuous

        continuousSum(root)

        return res
