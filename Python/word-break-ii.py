#submitted 03/19/2021

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
            whee = self.findWord(s, wordDict)
            i = 0
            while i < len(whee):
                whee[i] = whee[i].strip()
                i += 1
            return whee


    def findWord(self, s, wordDict):
        if s == "":
            return [""]
        returnarr = []
        for word in wordDict:
            if s.startswith(word):
                potato = s[(len(word)):]
                #print(potato)
                second = (self.findWord(potato, wordDict))
                #print(second)
                for elem in second:
                    returnarr.append(word + " " + elem)
        return returnarr