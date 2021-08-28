#submitted 24/08/2021

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        source = Counter()
        dest = Counter()
        
        if len(word1) != len(word2):
            return False
        
        for letter in word1:
            source[letter] += 1
        
        for letter in word2:
            dest[letter] += 1
            
        sourcedict = dict(source)
        destdict = dict(dest)
        sourcechars = []
        destchars = []
        
        for key in sourcedict:
            if key not in destdict:
                return False
            sourcechars.append(sourcedict[key])
        for key in destdict:
            if key not in sourcedict:
                return False
            destchars.append(destdict[key])
        
        sourcechars.sort()
        destchars.sort()
        
        for i in range(len(sourcechars)):
            if sourcechars[i] != destchars[i]:
                return False
        
        return True
        
        
        