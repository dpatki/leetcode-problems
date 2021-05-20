#submitted 16/05/2021
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        bounces = 0
        if q == 0:
            return 0
        elif q == p:
            return 1
        ypos = q
        while ypos % p != 0:
            ypos += q
            bounces += 1
  
        if (bounces % 2) == 1:
            return 2
  
        res = ypos / p
        if (res % 2) == 0:
            return 0

        return 1