#submitted 18/05/2022

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        output = []
        negs = []
        for elem in asteroids:
            if elem > 0:
                output.append(elem)
            else:
                while output and -elem > output[-1]:
                    output.pop()
                if not output:
                    negs.append(elem)
                elif output and -elem == output[-1]:
                    output.pop()
                
        return negs + output
        