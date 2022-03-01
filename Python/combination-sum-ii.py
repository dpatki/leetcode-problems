#submitted 28/02/2022
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        best = []
        uniques = list(set(candidates))
        def traverse(nums, unused):
           
            if sum(nums) == target:
                best.append(copy.deepcopy(nums))
                return
            if sum(nums) > target:
                return 
           
            for elem in uniques:
                if unused[elem] > 0:
                    nums.append(elem)
                    unused[elem] -= 1
                    traverse(nums, unused)
                    nums.pop()
                    unused[elem] += 1
        stuff = Counter(candidates)
        traverse([], stuff)
        for i in range(len(best)):
            thing = sorted(best[i])
            best[i] = tuple(thing)
        
        return list(set(best))