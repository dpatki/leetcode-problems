#submitted 12/29/2020
class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        returnme = []
        dicty = { }
        dicty[0] = a
        dicty[1] = b
        dicty[2] = c
        if (max(a, b, c) == a):
            dicty[0] -= 1
            returnme.append('a')
        elif(max(a, b, c) ==  b):
            dicty[1] -= 1
            returnme.append('b')
        else:
            dicty[2] -= 1
            returnme.append('c')

        if max(dicty[0], dicty[1], dicty[2]) == 0:
            return ''.join(returnme)
        if (max(dicty[0], dicty[1], dicty[2]) == dicty[0]):
            dicty[0] -= 1
            returnme.append('a')
        elif (max(dicty[0], dicty[1], dicty[2]) == dicty[1]):
            dicty[1] -= 1
            returnme.append('b')
        elif (max(dicty[0], dicty[1], dicty[2]) == dicty[2]):
            dicty[2] -= 1
            returnme.append('c')


        while max(dicty[0], dicty[1], dicty[2]) != 0:
            if (max(dicty[0], dicty[1], dicty[2]) == dicty[0]):
                if returnme[-1] == returnme[-2] and returnme[-2] == 'a':
                    if (max(dicty[1], dicty[2]) == 0):
                        return ''.join(returnme)
                    elif max(dicty[1], dicty[2]) == dicty[1]:
                        dicty[1] -= 1
                        returnme.append('b')
                    else:
                        dicty[2] -= 1
                        returnme.append('c')
                else:
                    dicty[0] -= 1
                    returnme.append('a')
            elif (max(dicty[0], dicty[1], dicty[2]) == dicty[1]):
                if returnme[-1] == returnme[-2] and returnme[-2] == 'b':
                    if (max(dicty[0], dicty[2]) == 0):
                        return ''.join(returnme)
                    elif max(dicty[0], dicty[2]) == dicty[0]:
                        dicty[0] -= 1
                        returnme.append('a')
                    else:
                        dicty[2] -= 1
                        returnme.append('c')
                else:
                    dicty[1] -= 1
                    returnme.append('b')
            elif (max(dicty[0], dicty[1], dicty[2]) == dicty[2]):
                if returnme[-1] == returnme[-2] and returnme[-2] == 'c':
                    if (max(dicty[1], dicty[0]) == 0):
                        return ''.join(returnme)
                    elif max(dicty[1], dicty[0]) == dicty[1]:
                        dicty[1] -= 1
                        returnme.append('b')
                    else:
                        dicty[0] -= 1
                        returnme.append('a')
                else:
                    dicty[2] -= 1
                    returnme.append('c')

        return ''.join(returnme)
