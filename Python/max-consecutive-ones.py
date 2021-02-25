#sumbitted 12/20/2020
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tempcounter= 0
        counter = 0
        i = 0
        while (i < len(nums)):
            if (nums[i] == 1):
                tempcounter = tempcounter + 1
                if (tempcounter > counter):
                    counter = tempcounter
            else:
                tempcounter = 0
            i = i + 1
        
        return counter
        