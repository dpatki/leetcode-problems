#submitted 01/24/2021
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        summ = sum(nums)
        if summ == len(nums):
            return len(nums) - 1
        if summ == 0:
            return 0

        curr = 0
        runs = []
        for thing in nums:
            if thing == 1:
                curr += 1
            if thing == 0:
                runs.append(curr)
                curr = 0
        runs.append(curr)
        best = 0
        curr = 0
        i = 0
        while (i < len(runs) - 1):
            curr = runs[i] + runs[i+1]
            if curr > best:
                best = curr
            i += 1
        return best