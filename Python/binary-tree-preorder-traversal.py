#submitted 12/09/2021
class Solution:
    values = []
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.values = []
        def helper(node):
            if not node:
                return
            self.values.append(node.val)
            helper(node.left)
            helper(node.right)
        helper(root)
        return self.values