#submitted 15/10/2021
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secretnums = Counter()
        guessnums = Counter()
        bulls = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                secretnums[secret[i]] += 1
                guessnums[guess[i]] += 1
        cows = 0
        for i in range(10):
            cows += min(secretnums[str(i)], guessnums[str(i)])
        
        final = str(bulls) + "A" + str(cows) + "B"
        return final