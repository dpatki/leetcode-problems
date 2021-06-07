#submitted 03/05/2021
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        newarr = [i + nums[i] for i in range(len(nums))]
        best = nums[0]
        while best < len(nums)-1:
            newbest = max(newarr[:(best+1)])
            if newbest == best:
                return False
            best = newbest
            
            
        return True