#submitted 12/31/2020
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        copy = nums
        maxi = max(copy)
        copy.remove(maxi)
        maxi2 = max(copy)
        
        return (maxi-1)*(maxi2-1)