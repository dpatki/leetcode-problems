#submitted 31/21/2021
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rights = [1]
        lefts = [1]
        for i in range(1, len(nums)):
            rights.append(rights[-1]*nums[i-1])
            lefts.append(lefts[-1]*nums[len(nums) - i])
        lefts.reverse()
        output = []
        for i in range(len(nums)):
            output.append(rights[i]*lefts[i])
        
            
        return output