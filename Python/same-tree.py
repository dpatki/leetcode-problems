#submitted 13/02/2022
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def traverse(p, q):
            if not p and not q:
                return True
            if not p:
                return False 
            if not q: 
                return False 
            if p.val != q.val:
                return False
            return traverse(p.left, q.left) and traverse(p.right, q.right)
        return traverse(p, q)