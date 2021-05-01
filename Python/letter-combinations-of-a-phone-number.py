#submitted 03/21/2021
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        mappings = [['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
        returnarr = []
        #if digits[0] == '1' or digits[0] == '0':
        #    return self.letterCombinations(digits[1:])
        prevs = self.letterCombinations(digits[1:])
        charss = mappings[int(digits[0])-2]
        if prevs == []:   
            for elem in charss:
                prevs.append(elem)
            return prevs
        for elem in prevs:
            for thing in charss:
                returnarr.append(thing+elem)
        
        return returnarr
            