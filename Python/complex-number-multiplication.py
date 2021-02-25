#submitted 01/23/2021
class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        num1 = a.split('+')
        num2 = b.split('+')
        a1 = int(num1[0])
        b1 = int(num2[0])
        a2 = int(num1[1].replace('i', ''))
        b2 = int(num2[1].replace('i', ''))
        real = a1*b1 - a2*b2
        imag = a1*b2 + a2*b1
        newstr = str(real) + '+' + str(imag) + 'i'
        return newstr