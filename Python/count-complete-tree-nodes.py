#submitted 09/10/2021
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def lefttraverse(node):
            if not node:
                return 0
            return lefttraverse(node.left) + 1
        
        def childdepth(node):
            if not node:
                return 0
            lefty = lefttraverse(node.left)
            righty = lefttraverse(node.right)
            res = 0
            if lefty == righty:
                res = childdepth(node.right)
                res += 2 ** lefty
            else:
                res = childdepth(node.left)
                res += 2 ** righty
            return res
        
        return childdepth(root)