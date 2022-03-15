#submitted 13/03/2022
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stackS = []
        stackT = []
        for elem in s:
            if elem != "#":
                stackS.append(elem)
            elif len(stackS) != 0:
                stackS.pop()
        for elem in t:
            if elem != "#":
                stackT.append(elem)
            elif len(stackT) != 0:
                stackT.pop()
       
        s = "".join(stackS)
        t = "".join(stackT)
       
        if s != t:
            return False
        return True