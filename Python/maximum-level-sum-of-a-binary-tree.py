#submitted 08/08/2021

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        best = 1
        bestsum = root.val
        counter = 1
        summ = 0
        queue = [root]
        newqueue = []
        while queue:
            for elem in queue:
                summ += elem.val
                if elem.left:
                    newqueue.append(elem.left)
                if elem.right:
                    newqueue.append(elem.right)
            print(summ, bestsum)
            if summ > bestsum:
                best = counter
                bestsum = summ
            
            summ = 0
            counter += 1
            queue = newqueue
            newqueue = []
        
        return best
            