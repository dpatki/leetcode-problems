#submitted 01/01/2021
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        note = {}
        mag = {}
        for i in ransomNote:
            if i not in note:
                note[i] = 1
            else:
                note[i] += 1
        for i in magazine:
            if i not in mag:
                mag[i] = 1
            else:
                mag[i] += 1
        print(mag)
        print(note)
        for key in note:
            if key not in mag:
                return False
            if note[key] > mag[key]:
                return False
        return True