# submitted 12/30/2020
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) +1
        total = n*(n-1) / 2
        summ = 0
        for i in nums:
            summ += i
        return total - summ