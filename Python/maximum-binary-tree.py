#submitted 04/01/2022
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(arr, parent):
            if len(arr) == 0:
                return None
            parent.val = max(arr)
            index = arr.index(parent.val)
            
            left = TreeNode(-1, None, None)
            right = TreeNode(-1, None, None)
            
            lefty = helper(arr[:index], left)
            righty = helper(arr[index+1:], right)
            #print(lefty, righty)
            
            parent.left = left if left.val != -1 else None
            parent.right = right if right.val != -1 else None
        head = TreeNode()
        helper(nums, head)
        return head
            