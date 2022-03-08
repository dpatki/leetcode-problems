#submitted 06/03/2022
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n > 45:
            return 
        if n < k*(k-1)/2:
            return 

        best = []
        
        def traverse(nums, i):
           
            if sum(nums) == n:
                if len(nums) == k:
                    best.append(copy.deepcopy(nums))
                return
            if sum(nums) > n or len(nums) == k:
                return 
            for j in range(i, 10):
                nums.append(j)
                traverse(nums, j+1)
                nums.pop()
              
        
        traverse([], 1)
        for i in range(len(best)):
            thing = sorted(best[i])
            best[i] = tuple(thing)
        
        return list(set(best))