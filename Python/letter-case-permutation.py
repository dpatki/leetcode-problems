#submitted 18/02/2022
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = [""]
        for chara in s:
            cur = []
            if chara.isalpha():
                upper = chara.upper()
                lower = chara.lower()
                for elem in res:
                    cur.append(elem+upper)
                    cur.append(elem+lower)
                res = cur
            else:
                for i in range(len(res)):
                    res[i] = res[i]+chara
        
        return res