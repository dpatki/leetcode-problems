#submitted 23/02/2022

class Solution:
    best = 0
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def helper(node):
            if not node:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            lefty = node.left.val if node.left else None
            righty = node.right.val if node.right else None
            cur = 1
            track = 0
            if lefty == node.val:
                cur += left
                track = left
            if righty == node.val:
                cur += right
                track = max(track, right)
            self.best = max(self.best, cur)
            return track + 1
        helper(root)
        return self.best - 1