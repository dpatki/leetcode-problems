#submitted 03/07/21

class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        output = []
        if len(s) <= 2:
            return []
        run = 0
        for i in range(0, len(s)-2):
            char1 = s[i]
            char2 = s[i+1]
            char3 = s[i+2]
            if (char1 == char2) and (char2 == char3):
                run += 1
            else:
                if run > 0:
                    startin = i - run
                    endin = i + 1
                    output.append([startin, endin])
                run = 0
        if run > 0:
            startin = len(s) - 2 - run
            endin = len(s) -1
            output.append([startin, endin])
        return output
