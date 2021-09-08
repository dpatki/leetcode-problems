#submitted 05/09/2021

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if (nums[i] % 2 == 0 and i % 2 == 0) or (nums[i] % 2 == 1 and i % 2 == 1):
                continue
            elif nums[i] % 2 == 1:
                j = i + 1
                while nums[j] % 2 != 0:
                    j += 1
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
            else:
                j = i + 1
                while nums[j] % 2 == 0:
                    j += 1
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp

        return nums