#submitted 03/14/2021

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        left = 0
        right = len(nums) - 1
        while (left < right):
            mid = int((left + right)/2)
            if (nums[mid] > nums[mid + 1]):
                right = mid
            else:
                left = mid +1
        return left