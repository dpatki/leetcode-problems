# submitted 09/05/2021
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        start = 0
        end = 1
        curmin = min(nums[start:end])
        curmax = max(nums[start:end])
        best = 1
        while end < len(nums):
            if nums[end] > curmax:
                curmax = nums[end]
            elif nums[end] < curmin:
                curmin = nums[end]
            if (curmax - curmin) > limit:
                start += 1
                curmin = min(nums[start:end+1])
                curmax = max(nums[start:end+1])

            end += 1

            if (end - start) > best:
                best = end-start
        return best