#submitted 25/01/2022
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        best = nums[0]
        current = nums[0]
        mini = nums[0]
        for i in range(1, len(nums)):
            newcurrent = max(nums[i], current * nums[i], mini * nums[i])
            newmini = min(nums[i], current * nums[i], mini * nums[i])
            current = newcurrent
            mini = newmini
            best = max(best, current)
            print(current, mini, best)
        return best