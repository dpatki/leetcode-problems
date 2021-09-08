#submitted 03/09/2021

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def leftmost():
            start = 0
            end = len(nums) - 1
            while start <= end:
                test = (start + end) // 2
                if nums[test] < target :
                    start = test + 1
                else:
                    end = test - 1

            return start
        
        def rightmost():
            start = 0
            end = len(nums) - 1
            while start <= end:
                test = math.ceil((start + end) / 2)
                if nums[test] > target:
                    end = test - 1
                else:
                    start = test + 1
            
            return end
        
        start = 0
        end = len(nums) - 1
        while start <= end:
            test = (start + end) // 2
            if nums[test] > target:
                    end = test - 1
            elif nums[test] == target:
                left = leftmost()
                right = rightmost()
                return [left, right]
            else:
                start = test + 1

        return [-1, -1]
        