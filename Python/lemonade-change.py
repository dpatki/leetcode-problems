#submitted 01/07/2021
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {5:0, 10:0}
        for i in bills:
            #print(change)
            if i == 5:
                change[5] += 1
            if i == 10:
                if change[5]  <= 0:
                    return False
                change[5] -= 1
                change[10] += 1
            if i == 20:
                if change[10] > 0:
                    if change[5] > 0:
                        change[5] -= 1
                        change[10] -= 1
                    else: 
                        return False
                else:
                    if change[5] < 3:
                        return False
                    else:
                        change[5] -= 3
        
        return True