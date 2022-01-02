#submitted 31/12/2021
class Solution:
    paths = 0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        def helper(node):
            if not node:
                return
            tester(node, 0)
            helper(node.left)
            helper(node.right)
           
        
        def tester(node, partialSum):
            if not node:
                return
            if (partialSum + node.val == targetSum):
                self.paths += 1
                #print(node.val)
            tester(node.left, partialSum + node.val)
            tester(node.right, partialSum + node.val)
        
        helper(root)
        return self.paths
        