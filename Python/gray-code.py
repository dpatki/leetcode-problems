#submitted 28/03/2021
class Solution:
    def grayCode(self, n: int) -> List[int]:
        listicle = ['0', '1']
        
        while len(listicle) != 2**n:
            reversi = copy.deepcopy(listicle)
            reversi.reverse()
            #print(reversi)
            i = 0
            while i < len(reversi):
                listicle[i] = '0' + listicle[i]
                reversi[i] = '1' + reversi[i]
                i += 1
            #print(listicle, reversi)
            
            for elem in reversi:
                listicle.append(elem)
                
        
        i = 0
        while i < len(listicle):
            listicle[i] = int(listicle[i], 2)
            i += 1
        
        return listicle