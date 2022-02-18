#submitted 17/02/2022
class Solution:
    best = -math.inf
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def traverse(node):
            if not node:
                return 0
            left = traverse(node.left)
            right = traverse(node.right)
            self.best = max(self.best, node.val, node.val+left, node.val+right, node.val+left+right)
            #print(self.best)
            return max(node.val, node.val, node.val+left, node.val+right)
        traverse(root)
        return self.best