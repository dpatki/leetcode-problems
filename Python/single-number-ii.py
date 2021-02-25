#submitted 12/28/2020
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i = 0
        while i < (len(nums) -1):
            if nums[i] == nums[i+1]  and nums[i+1] == nums[i+2]:
                nums.pop(0)
                nums.pop(0)
                nums.pop(0)
                #print(nums)
            else:
                break
        return nums[0]