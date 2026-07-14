class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preorder = preorder
        self.inorder = inorder
        self.pre_index = 0
        self.in_index = 0

        return self.build_subtree(stop=float('inf'))

    def build_subtree(self, stop: float) -> Optional[TreeNode]:
        if self.pre_index == len(self.preorder):
            return None

        if self.inorder[self.in_index] == stop:
            self.in_index += 1
            return None

        root = TreeNode(self.preorder[self.pre_index])
        self.pre_index += 1

        root.left = self.build_subtree(stop=root.val)

        root.right = self.build_subtree(stop=stop)

        return root