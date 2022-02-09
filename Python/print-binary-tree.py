#submitted 08/02/2022
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        
        def getHeight(node):
            if not node:
                return 0
            return max(getHeight(node.left), getHeight(node.right)) + 1 
        height = getHeight(root)
        matrix = [[""] * (2**(height)-1) for i in range(height)]
        def traverse(node, position, level):
            if not node:
                return 
            matrix[level][position] = str(node.val)
            traverse(node.left, position-2**(height-level-2), level+1)
            traverse(node.right, position+2**(height-level-2), level+1)
        traverse(root, (len(matrix[0]) - 1)//2, 0)
        return matrix 
