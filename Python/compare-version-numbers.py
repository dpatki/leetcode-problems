#submitted 02/13/2021
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        i = 0
        while i < len(v1):
            v1[i] = int(v1[i])
            i += 1
            
        i = 0 
        while i < len(v2):
            v2[i] = int(v2[i])
            i += 1
        
        print(v1, v2)
        
        if len(v1) > len(v2):
            while len(v1) > len(v2):
                v2.append(0)
        elif (len(v1)) < len(v2):
            while len(v1) < len(v2):
                v1.append(0)
        
        for i in range(0,len(v1)):
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1
        
        return 0
            