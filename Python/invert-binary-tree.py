#submitted 13/01/2022
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node):
            if not node:
                return
            helper(node.right)
            helper(node.left)
            temp = node.right
            node.right = node.left
            node.left = temp
        
        helper(root)
        return root