# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        levels = deque([root])
        right_view = []
        while levels:
            right_view.append(levels[-1].val)
            n = len(levels)
            for _ in range(n):
                node = levels.popleft()
                if node.left:
                    levels.append(node.left)
                if node.right:
                    levels.append(node.right)
        return right_view
