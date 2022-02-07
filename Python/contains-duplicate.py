#submitted 18/01/2022
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        c = Counter(nums)
        if c.most_common(1)[0][1] > 1:
            return True
        return False