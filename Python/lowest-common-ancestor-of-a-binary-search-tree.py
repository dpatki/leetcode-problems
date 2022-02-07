#submitted 12/01/2022
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def hasDescendant(node, target):
            if node:
                if node.right == target or node.left == target or node == target:
                    return True
                return hasDescendant(node.right, target) or hasDescendant(node.left, target)
            return False
        def helper(node):
            if hasDescendant(node.right, p) and hasDescendant(node.right, q):
                return helper(node.right)
            elif hasDescendant(node.left, p) and hasDescendant(node.left, q):
                return helper(node.left)
            return node
        return helper(root)