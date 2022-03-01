#submitted 28/02/2022
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        best = []
        def traverse(nums):
           
            if sum(nums) == target:
                best.append(copy.deepcopy(nums))
                return
            if sum(nums) > target:
                return 
            for elem in candidates:
                nums.append(elem)
                traverse(nums)
                nums.pop()
        
        traverse([])
        for i in range(len(best)):
            thing = sorted(best[i])
            best[i] = tuple(thing)
        
        return list(set(best))