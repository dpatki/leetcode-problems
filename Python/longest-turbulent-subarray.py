#submitted 02/05/2021
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        best = 1
        if len(arr) == 1:
            return 1
        if len(arr) == 2:
            if arr[0] == arr[1]:
                return 1
            else:
                return 2
        i = 1
        current = 0
        while i < (len(arr) - 1):
            if best < 2:
                if (arr[i-1] > arr[i] or arr[i] > arr[i+1] or arr[i] < arr[i-1] or arr[i] < arr[i+1]):
                    #print(sup)
                    best = 2
            if arr[i-1] < arr[i] and arr[i] > arr[i+1]:
                current += 1
            elif arr[i-1] > arr[i] and arr[i] < arr[i+1]:
                current += 1
            else:
                current = 0
            if current + 2 > best and current != 0:
                best = current + 2
            i += 1

        return best