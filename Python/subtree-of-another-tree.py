#submitted 24/08/2022

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subroot:
            return True
        if not subRoot:
            return True
        if not root:
            return False
        def helper(parent, test):
            if not parent and not test:
                return True
            if not parent:
                return False
            if not test:
                return False
            if parent.val != test.val:
                return False
            return helper(parent.left, test.left) and helper(parent.right, test.right)
        if helper(root, subRoot):
            return True
        def helpertwo(parent, test):
            if not parent and not test:
                return True
            if not parent:
                return False
            if not test:
                return False
            if parent.val != test.val:
                return helpertwo(parent.left, test) or helpertwo(parent.right, test)
            return helper(parent, test) or helpertwo(parent.left, test) or helpertwo(parent.right, test)
        return helpertwo(root, subRoot)