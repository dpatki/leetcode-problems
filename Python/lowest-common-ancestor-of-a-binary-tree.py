#submitted 17/01/2022
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def getNode(node, target):
            if not node:
                return False
            if node == target:
                return True
            return getNode(node.left, target) or getNode(node.right, target)
        
        def helper(node):
            if not node:
                return None
            left = helper(node.left)
            right = helper(node.right)
            
            if left:
                return left
            if right:
                return right
            
            if getNode(node, p) and getNode(node, q):
                return node
            
            return None
        
        return helper(root)
            