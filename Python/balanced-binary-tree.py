#submitted 30/05/2021
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        if root == None:
            return True
        if (not self.isBalanced(root.right)) or (not self.isBalanced(root.left)):

            return False
        if abs(self.maxDepth(root.right) - self.maxDepth(root.left)) > 1:

            return False
        return True

    def maxDepth(self, node):
        if node == None:
            return 0
        return max(self.maxDepth(node.right), self.maxDepth(node.left)) + 1