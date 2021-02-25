#submitted 01/23/2021
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n > len(flowerbed):
            return False
        i = 0
        flowers = 0
        while i < len(flowerbed):
            if flowerbed[i] == 0:
                if i > 0 and i < (len(flowerbed)-1):
                    if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        flowers += 1
                elif i == 0:
                    if (i+1) > len(flowerbed) - 1:
                        flowers += 1
                    elif flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        flowers += 1
                elif i == (len(flowerbed) - 1):
                    if flowerbed[i-1] == 0:
                        flowerbed[i] = 1
                        flowers += 1
            i += 1
        print(flowers)
        print(flowerbed)
        if n > flowers:
            return False
        else: 
            return True