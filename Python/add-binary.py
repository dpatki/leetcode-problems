#submitted 22/08/2022

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        res = ""
        reva = a[::-1]
        revb = b[::-1]
        for i in range(max(len(a), len(b))):
            if i < len(a):
                carry += int(reva[i])
            if i < len(b):
                carry += int(revb[i])
            res += str(carry % 2)
            if carry > 1:
                carry = 1
            else:
                carry = 0
        if carry == 1:
            res += "1"
        return res[::-1]