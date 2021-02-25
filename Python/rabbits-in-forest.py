#submitted 01/04/2021
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        colours = {}
        for i in answers:
            if i not in colours:
                colours[i] = 1
            else:
                colours[i] += 1
        
        ans = 0
        #print(colours)
        for item in colours:    
            #print(item)
            #print(colours[item])
            #ting = (math.ceil((colours[item])/(item+1)))
            #print(ting)
            ans += (item+1) * math.ceil(colours[item]/(item+1))
        
        return int(ans)
        