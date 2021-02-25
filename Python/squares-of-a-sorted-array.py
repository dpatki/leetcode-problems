#submitted 12/23/2020
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0
        while (i < len(nums)):
            nums[i] = nums[i] ** 2
            i = i +1
        nums.sort()
        return nums
        