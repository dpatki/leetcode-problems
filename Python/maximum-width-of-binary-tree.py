#submitted 13/02/2022

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        levels = []
        
        def search(node, binary, level):
            if not node:
                return 
            if len(levels) <= level:
                levels.append([int(binary, 2), int(binary, 2)])
            else:
                levels[level] = [min(int(binary, 2), levels[level][0]), max(int(binary, 2), levels[level][1])]
            search(node.left, binary  + "0", level+1)
            search(node.right, binary + "1", level+1)
        
        search(root, "0", 0)
        
        best = 0
        for level in levels:
            best = max(best, level[1]-level[0]+1)
        
        return best