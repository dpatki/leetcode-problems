#submitted 27/01/2022
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
       
        summ = sum(nums)
        initial = 0
        for i in range(len(nums)):
            initial += i * nums[i]
        best = initial
        for i in range(len(nums)-1, 0, -1):
            initial = initial + summ - (len(nums)) * nums[i]
            #print(initial)
            best = max(best, initial)
        return best
            