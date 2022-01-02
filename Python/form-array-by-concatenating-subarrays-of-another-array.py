#submitted 31/21/2021
class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        for elem in groups:
            if len(nums) == 0:
                return False
            while len(nums) > 0:
                #print("hello")
                while nums[0] != elem[0]:
                    nums.pop(0)
                    if len(nums) == 0:
                        return False
                if nums[0:len(elem)] == elem:
                    nums = nums[len(elem):]
                    break
                else:
                    nums.pop(0)
                    if len(nums) == 0:
                        return False

        return True