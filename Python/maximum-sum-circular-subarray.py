#submitted 08/02/2022
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        best = nums[0]
        current = nums[0]
        for i in range(1, len(nums)):
            newcurrent = max(nums[i], current + nums[i])
            current = newcurrent
            best = max(best, current)      
        mini = nums[0]
        current = nums[0]
        for i in range(1, len(nums)):
            newcurrent = min(nums[i], current + nums[i])
            current = newcurrent
            mini = min(mini, current)
        if mini == sum(nums):
            mini = 0
        return max(best, sum(nums)-mini)