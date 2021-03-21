#submitted 03/19/2021
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        letters = [0]*26
        for ch in s1:
            letters[ord(ch)-97] += 1
        i = 0
        map2 = [0]*26
        while i < len(s1):
            map2[ord(s2[i]) -97] += 1
            i+=1
        
        for i in range(0, len(s2)-len(s1)):
            if map2 == letters:
                return True
            print(letters, map2)
            
            map2[ord(s2[i]) - 97] -= 1
            
            map2[ord(s2[len(s1) + i]) -97] += 1
                
        if map2 == letters:
            return True
        return False
        