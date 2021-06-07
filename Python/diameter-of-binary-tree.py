#submitted 06/06/2021
class Solution:
    best = 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.best = 0
        def maxDepth(root):
            if not root:
                return 0
            left = maxDepth(root.left)
            right =  maxDepth(root.right)
            total = left+right
            self.best = max(total, self.best)
            return max(left, right) + 1
        maxDepth(root)
        return self.best