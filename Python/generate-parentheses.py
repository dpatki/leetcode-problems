#submitted 18/02/2022
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def driver(opens, closes, cur):
            if (opens == closes == 0):
                return [cur]
            lefts = []
            rights = []
            if opens > 0:
                lefts = driver(opens-1, closes+1, cur + "(" )
            if closes > 0:
                rights = driver(opens, closes-1, cur + ")" )
            return list(set(lefts + rights))
        return driver(n, 0, "")