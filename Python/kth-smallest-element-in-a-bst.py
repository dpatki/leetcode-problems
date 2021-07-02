#submitted 01/07/2021
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def traverse(node):
            if not node:
                return []
            lefts = traverse(node.left)
            rights = traverse(node.right)
            return lefts + [node.val] + rights
        stuff = traverse(root)
        return stuff[k-1]