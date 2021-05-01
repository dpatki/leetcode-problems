#submitted 28/03/2021
class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        cost = [-1]*n
        
        reds = defaultdict(list)
        blues = defaultdict(list)
        for elem in red_edges:
            if elem[0] not in reds:
                reds[elem[0]].append(elem[1])
            else:
                reds[elem[0]].append(elem[1])
        for elem in blue_edges:
            if elem[0] not in blues:
                blues[elem[0]].append(elem[1])
            else:
                blues[elem[0]].append(elem[1])

        seenr = [0]
        seenb = [0]
        queue = []
        for elem in reds[0]:
            queue.append([elem, 'red', 1])
            cost[elem] = 1
            seenr.append(elem)
        for elem in blues[0]:
            queue.append([elem, 'blue', 1])
            cost[elem] = 1
            seenb.append(elem)

        while len(queue) != 0:
            #print(queue)
            #print(cost)
            #print(seenr, seenb)
            elem = queue.pop(0)
            if elem[1] == 'blue': 
                for thingy in reds[elem[0]]:
                    if thingy not in seenr:
                        queue.append([thingy, 'red', elem[2] + 1])
                        if cost[thingy] == -1:
                            cost[thingy] = elem[2] + 1
                        elif cost[thingy] > elem[2]:
                            cost[thingy] = elem[2] + 1
                        seenr.append(thingy)
            else:
                for thingy in blues[elem[0]]:
                    if thingy not in seenb:
                        queue.append([thingy, 'blue', elem[2] + 1])
                        if cost[thingy] == -1:
                            cost[thingy] = elem[2] + 1
                        elif cost[thingy] > elem[2]:
                            cost[thingy] = elem[2] + 1
                        seenb.append(thingy)
        cost[0] = 0
        return cost