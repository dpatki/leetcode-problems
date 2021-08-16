#submitted 08/08/2021

class Solution:
    def reverseWords(self, s: str) -> str:
        things = s.split()
        revs = []
        for elem in things:
            revs.append(elem[::-1])

        thing2 = ""
        for elem in revs:
            thing2 += elem
            thing2 += " "
        return thing2[0:len(thing2)-1]