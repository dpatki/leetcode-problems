#submitted 02/21/2021
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        i = 0 
        while i < len(gas):
            tank = 0
            j = i
            k = 0
            while k < len(gas):
                tank += gas[j] - cost[j]
                if tank < 0:
                    break
                j += 1
                if j == len(gas):
                    j = 0
                if j == i:
                    return i
                
                k += 1
            i += 1
        
        return -1
        