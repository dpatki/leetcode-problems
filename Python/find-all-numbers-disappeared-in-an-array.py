#submitted 14/01/2022
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[(nums[i] % len(nums)-1)] += len(nums)
        print(nums)
        output = []
        for i in range(len(nums)):
            if nums[i] <= len(nums):
                output.append(i+1)
        print(output)
        return output