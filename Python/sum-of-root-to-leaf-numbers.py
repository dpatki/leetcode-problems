#submitted 06/06/2021
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        
        def listchildren(root):
            if not root:
                return None
            lefts = listchildren(root.left)
            rights = listchildren(root.right)
            if not lefts and not rights:
                return [str(root.val)]
                
            final = []
            if lefts:
                for elem in lefts:
                    final.append(str(root.val) + elem)
            if rights:
                for elem in rights:
                    final.append(str(root.val) + elem)
                    
            return final
        
        stuffs = listchildren(root)
        total = 0
        for elem in stuffs:
            total += int(elem)
            
        return total