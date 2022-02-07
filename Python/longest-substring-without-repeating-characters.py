#submitted 03/02/2022
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        best = 0
        contains = []
        while start < len(s):
            #print(s[start], s[end], contains)
            if s[start] not in contains:
                contains.append(s[start])
                start += 1
            else:
                contains.remove(s[end])
                end += 1
            best = max(start-end, best)
        return best