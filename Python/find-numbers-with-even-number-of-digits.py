#submitted 12/21/2020
class Solution(object):            
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 0
        for i in nums:
            counter2 = 0
            while (i >= 1):
                i = i /10
                counter2 = counter2 +1
            if ((counter2 % 2) == 0):
                counter = counter +1
        return counter