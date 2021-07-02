#submitted 27/06/2021
class Solution:
    def isValid(self, s: str) -> bool:
        stakc = []
        for elem in s:
            if elem in "({[":
                stakc.append(elem)
            else:
                if stakc:
                    check = stakc.pop()
                    if check == "(":
                        if elem != ")":
                            return False 
                    elif check == "{":
                        if elem != "}":
                            return False 
                    elif check == "[":
                        if elem != "]":
                            return False
                else:
                    return False
        if len(stakc) != 0:
            return False
        return True