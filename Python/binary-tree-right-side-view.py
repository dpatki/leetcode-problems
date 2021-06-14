# submitted 13/06/2021
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        dicty = defaultdict(list)
        def traverse(root, depth):
            if not root:
                return
            traverse(root.right, depth + 1)
            traverse(root.left, depth + 1)
            
             
            dicty[depth].append(root.val)
        
        traverse(root, 0)
        print(dicty)
        final = []
        i = 0
        while i in dicty:
            final.append(dicty[i][0])
            i += 1
        
        return final