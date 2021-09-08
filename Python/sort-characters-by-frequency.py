#submitted 29/08/2021

class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter()
        for chara in s:
            c[chara] += 1
        res = ""
        listicle = c.most_common()
        for entry in listicle:
            res += str(entry[0]) * entry[1]
        
        return res
        