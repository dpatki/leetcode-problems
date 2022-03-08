#submitted 01/03/2022
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
    
        def traverse(current, index):
            for i in range(index, len(nums)):
                result.append((current) + [nums[i]])
                traverse((current) + [nums[i]], i + 1)
        traverse([], 0)
        return result