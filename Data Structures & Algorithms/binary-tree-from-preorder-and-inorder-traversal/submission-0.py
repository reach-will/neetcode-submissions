# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        node = root
        if len(preorder) == 1:
            return root
        inorder_idx = inorder.index(preorder[0])
        if inorder_idx == 0:
            root.right = self.buildTree(preorder[1:], inorder[1:])
            return root
        root.left = self.buildTree(preorder[1:inorder_idx + 1], inorder[:inorder_idx])
        if inorder_idx == len(preorder) - 1:
            return root
        root.right = self.buildTree(preorder[inorder_idx + 1:], inorder[inorder_idx + 1:])
        return root