#submitted 12/25/2020
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        returnme = 0
        char = list(s)
        char.append('0')
        i = 0
        while (i < len(char)):
            if char[i] == 'M':
                returnme += 1000
            elif char[i] == 'D':
                returnme += 500
            elif char[i] == 'C':
                if char[i+1] == 'M':
                    returnme += 900
                    i +=1
                elif char[i+1] == 'D':
                    returnme += 400
                    i+=1
                else:
                    returnme +=100
            elif char[i] == 'L':
                returnme += 50
            elif char[i] == 'X':
                if char[i+1] == 'C':
                    returnme += 90
                    i += 1
                elif char[i+1] == 'L':
                    returnme += 40
                    i += 1
                else:
                    returnme += 10
            elif char[i] == 'V':
                #print("adding 5")
                returnme += 5
            elif char[i] == 'I':
                if char[i+1] == 'X':
                    returnme += 9
                    i += 1
                elif char[i+1] == 'V':
                    returnme += 4
                    i += 1
                else:
                    returnme += 1
            i += 1
        return returnme
                