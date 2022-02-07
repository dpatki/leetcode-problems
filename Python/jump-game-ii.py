#submitted 05/02/2022
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        cur = nums[0]
        prev = 0
        best = 0
        total = 1
        while cur < len(nums)-1:
            print(prev, cur, best)
            for i in range(prev+1, min(len(nums), cur + 1)):
                if best <= nums[i] + i:
                    prev = i
                    best = nums[i] + i
            cur = prev + nums[prev]
            total += 1
        return total