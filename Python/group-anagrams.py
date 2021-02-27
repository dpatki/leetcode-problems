#submitted 02/26/2021
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        total = {}
        for elem in strs:
            lenn = len(elem)
            if lenn not in total:
                total[lenn] = [elem]
            else:
                total[lenn].append(elem)

        total2 = []

        for key in total:
            if len(total[key]) == 1:
                total2.append([total[key][0]])
                continue

            for i in range(0, len(total[key])):
                letters = {}
                for chars in total[key][i]:
                    if chars not in letters:
                        letters[chars] = 1
                    else:
                        letters[chars] += 1
                total[key][i] = [total[key][i], letters]
            #print(total[key])

            while len(total[key]) != 0:
                grams = []
                first = total[key][0][1]
                i = 0
                removeme = []
                for elem in (total[key]):
                    #print(elem, first)
                    if elem[1] == first:
                        grams.append(elem[0])
                        removeme.append(i)
                    i += 1
              #print(grams)
                total2.append(grams)
                removeme.reverse()
                for thing in removeme:
                    total[key].pop(thing)

        return total2