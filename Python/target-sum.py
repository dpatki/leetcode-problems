#submitted 13/03/2022
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = 0
        things = []
        for i in range(len(nums)+1):
            things.append(Counter())
        things[0][0] = 1
        for i in range(0, len(nums)):
            #print(things[i])
            for key in list(things[i]):
                things[i+1][key-nums[i]] += things[i][key]
                things[i+1][key+nums[i]] += things[i][key]
        
        return things[-1][target]