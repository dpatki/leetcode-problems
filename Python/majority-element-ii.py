# submitted 28/05/2021
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nummy = {}
        for elem in nums:
            if elem not in nummy:
                nummy[elem] = 1
            else:
                nummy[elem] += 1
        result = []
        for key in nummy:
            if nummy[key] > (len(nums)//3):
                result.append(key)
        return result