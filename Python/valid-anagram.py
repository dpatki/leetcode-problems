#submitted 22/08/2022

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        esses = Counter(s)
        tees = Counter(t)
        esses.subtract(tees)
        if len(sorted(esses.elements())) != 0:
            return False
        return True