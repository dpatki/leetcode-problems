#submitted 12/26/2020
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        boingo = len(nums) // 2
        elements = {}
        for i in nums:
            if i in elements:
                elements[i] += 1
            else:
                elements[i] = 1
        for item in list(elements):
            if elements[item] > boingo:
                return item
        #print(potato)
        #return potato[0]