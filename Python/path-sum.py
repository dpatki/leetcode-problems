# submitted 10/06/2021
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        def traverse(root):
            if not root:
                return None
            lefts = traverse(root.left)
            rights = traverse(root.right)
            
            if not lefts and not rights:
                return [root.val]
            final = []
            
            if lefts:
                for elem in lefts:
                    final.append(root.val + elem)
            if rights:
                for elem in rights:
                    final.append(root.val + elem)
            
            return final
        if not root:
            return False
        listicle = traverse(root)
        if targetSum not in listicle:
            return False
        return True