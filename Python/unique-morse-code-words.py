#submitted 03/19/2021
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        listicle = []
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for word in words:
            thingy = ""
            for ch in word:
                thingy += code[ord(ch)-97]
            if thingy not in listicle:
                listicle.append(thingy)
        
        return len(listicle)