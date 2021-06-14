# submitted 11/06/2021
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        summ = sum(nums)
        if summ < target:
            return 0
        if summ == target:
            return len(nums)
        maxx = max(nums)
        if maxx >= target:
            return 1

        start = 0
        end = 0
        best = len(nums)
        while (end < len(nums)):
    
            end += 1
            while sum(nums[start:end]) >= target:
                start += 1
            if (end-start) < best and sum(nums[start - 1:end]) >= target:
                best = end - start + 1

        return best