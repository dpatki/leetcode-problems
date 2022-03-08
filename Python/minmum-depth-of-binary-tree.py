#submitted 07/03/2022
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def traverse(node, level):
            if not node.left and not node.right:
                return level
            thing = math.inf
            if node.left:
                thing = traverse(node.left, level+1)
            if node.right:
                thing = min(thing, traverse(node.right, level + 1))
            return thing
        if not root:
            return 0
        return traverse(root, 0)+1