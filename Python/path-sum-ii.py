# submitted 10/06/2021
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        def traverse(root):
            if not root:
                return None
            lefts = traverse(root.left)
            rights = traverse(root.right)
            
            if not lefts and not rights:
                return [[root.val, [root.val]]]
            final = []
            
            if lefts:
                for elem in lefts:
                    final.append([root.val + elem[0], [root.val] + elem[1]])
            if rights:
                for elem in rights:
                    final.append([root.val + elem[0], [root.val] + elem[1]])
            
            return final
        if not root:
            return []
        listicle = traverse(root)
        final = []
        for thing in listicle:
            if thing[0] == targetSum:
                final.append(thing[1])
        
        return final