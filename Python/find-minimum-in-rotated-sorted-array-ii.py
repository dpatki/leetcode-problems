#submitted 01/02/2021
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums) - 1


        while (start <= end):
            if nums[start] < nums[end]:
                return nums[start]

            if start == end:
                return nums[start]

            m = start + (end - start)//2
            '''
            if nums[m] > nums[m+1]:
              return nums[m+1]
            '''
            if nums[start] < nums[m]:
                start = m +1
            elif nums[m] < nums[start]:
                end = m
            elif nums[start] == nums[m]:
                start += 1