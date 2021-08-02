# submitted 25/07/2021

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        length = len(arr)
        totals = {}
        for elem in arr:
            if elem not in totals:
                totals[elem] = 1
            else:
                totals[elem] += 1
        
        listicle = []
        #print(totals)
        for key in totals:
            listicle.append(totals[key])
        
        listicle.sort(reverse=True)
        
        total = 0
        for i in range(len(listicle)):
            total += listicle[i]
            if length <= total * 2:
                return i+1