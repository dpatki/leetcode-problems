#submitted 18/06/2021
class Solution:
    def countLargestGroup(self, n: int) -> int:
        def convertToSum(number):
            temp = str(number)
            summ = 0
            for elem in temp:
                summ += int(elem)
            return summ
  
        size = 0
        count = 0
        sizes = collections.defaultdict(list)
        for i in range(1, n+1):
            hash = convertToSum(i)
            sizes[hash].append(i)
            temp = len(sizes[hash])
            if temp > size:
                size = temp
                count = 1
            elif temp == size:
                count += 1
  
        return count