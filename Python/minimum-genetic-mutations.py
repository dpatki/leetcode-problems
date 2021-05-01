#submitted 03/21/2021

class Solution:
    def minMutation(self,start, end, bank):
        muts = defaultdict(list)
        if start not in bank:
            bank.append(start)
        for thing in bank:
            muts[thing] = self.neigh(thing, bank)
            #print(muts)
        return self.tracking(start, end, muts, 0, [])


    def tracking(self, cur, end, muts, count, seen):
        temparr = []
        for seq in muts[cur]:
            if seq == end:
                return count+1
            if seq not in seen:
                seen.append(seq)
                temparr.append(self.tracking(seq, end, muts, count+1, copy.deepcopy(seen)))
        best = -1
        if temparr == []:
            return -1
        for item in temparr:
            if best == -1:
                best = item
            elif item < best and item!= -1:
                best = item
        return best
  

    def neigh (self, elem, bank):
        returnarr = []
        for seq in bank:
            #print(elem, seq)
            diffs = 0
            for i in range(0,8):
                if seq[i] != elem[i]:
                    diffs += 1
            if diffs == 1:
                #print(seq)
                returnarr.append(seq)
        return returnarr