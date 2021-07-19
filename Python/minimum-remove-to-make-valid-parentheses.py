#submitted 02/07/2021
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        removes = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if stack:
                    stack.pop()
                else:
                    removes.append(i)
  
        final = removes + stack

        stringy = ""

        for i in range(len(s)):
            if i not in final:
                stringy += s[i]
  
        return stringy