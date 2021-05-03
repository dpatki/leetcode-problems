#submitted 02/05/2021
class Solution:
    def alpha(self, num):
        return chr(int(num) + ord('a') - 1)

    def freqAlphabets(self, s):
        solution = []
        mode = False
        listicle = list(s)
        while len(listicle) != 0:
            stuff = []
            thing = ""
            if mode:
                stuff += listicle.pop()
                stuff += listicle.pop()
                stuff.reverse()
                for chars in stuff:
                    thing += chars
                mode = False
            else:
                stuff = [listicle.pop()]
                if stuff[0] == "#":
                    mode = True
                    continue
                thing += stuff[0]
    
            output = self.alpha(thing)
            solution.append(output)
  
        solution.reverse()
        final = "".join(solution)
        return final