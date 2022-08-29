#submitted 27/06/2022

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        res = []
        counter = Counter(p)
        length = len(p)
        for i in range(length):
            counter[s[i]] -= 1
            if counter[s[i]] == 0:
                del counter[s[i]]
            if len(list(counter)) == 0:
                res.append(0)
        for i in range(len(s) - length):
           
            counter[s[i]] += 1
            if counter[s[i]] == 0:
                del counter[s[i]]
            counter[s[i+length]] -= 1
            if counter[s[i+length]] == 0:
                del counter[s[i+length]]
            if len(list(counter)) == 0:
                res.append(i+1)
        return res