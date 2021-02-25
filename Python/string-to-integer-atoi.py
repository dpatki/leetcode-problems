#submitted 02/07/2021
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        sign = 1
        out = [0]
        i = 0
        if len(s) == 0:
            return 0
        if s[0] == '-':
            sign = 0
            i += 1
        elif s[0] == '+':
            i += 1
        while (i < len(s)) and (s[i].isdecimal()):
            digit = s[i]
            out.append(digit)
            i += 1
        
        stringy = ""
        for dig in out:
            stringy += str(dig)
        
        potato = int(stringy)
        if sign == 0:
            potato = -potato
        if potato > (2**31 - 1):
            potato = 2**31 - 1
        elif potato < (-2**31):
            potato = - 2**31
        return potato
        