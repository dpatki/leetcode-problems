#submitted 01/31/2021
class Solution:
    def minimumDeletions(self, s: str) -> int:
        counter = 0
        bbefore = 0
        i = 0
        while i < len(s):

            if (s[i] == "a"):
                counter = min(counter+1, bbefore)  
            else:   
                bbefore += 1
            i += 1


        return counter
        