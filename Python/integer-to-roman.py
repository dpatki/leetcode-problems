#submitted 12/25/2020
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        returnstr = ""
        while (num > 0):
            if (num >= 1000):
                returnstr = returnstr + 'M'
                num = num - 1000
            elif (num >= 900):
                returnstr = returnstr + 'CM'
                num = num - 900
            elif (num >= 500):
                returnstr = returnstr + 'D'
                num = num - 500
            elif (num >= 400):
                returnstr = returnstr + 'CD'
                num = num - 400
            elif (num >= 100):
                returnstr = returnstr + 'C'
                num = num - 100
            elif (num >= 90):
                returnstr = returnstr + 'XC'
                num = num - 90
            elif (num >= 50):
                returnstr = returnstr + 'L'
                num = num - 50
            elif (num >= 40):
                returnstr = returnstr + 'XL'
                num = num - 40
            elif (num >= 10):
                returnstr = returnstr + 'X'
                num = num - 10
            elif (num >= 9):
                returnstr = returnstr + 'IX'
                num = num - 9
            elif (num >= 5):
                returnstr = returnstr + 'V'
                num = num - 5
            elif (num >= 4):
                returnstr = returnstr + 'IV'
                num = num - 4
            elif (num >= 1):
                #print("hi")
                returnstr = returnstr + 'I'
                num = num - 1
        return returnstr