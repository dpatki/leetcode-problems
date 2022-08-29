#submitted 22/08/2022

class Solution:
    def longestPalindrome(self, s: str) -> int:
        total = 0
        letters = Counter(s)
        oddly = False
        print(letters.most_common())
        for pair in letters.most_common():
            if pair[1] %2 == 0:
                total += pair[1]
            else:
                if not oddly:
                    total += pair[1]
                    oddly = True
                else:
                    total += pair[1] - 1
        return total