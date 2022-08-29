#submitted 07/06/2022

class RandomizedSet:

    def __init__(self):
        self.counter = Counter()
        self.list = []

    def insert(self, val: int) -> bool:
        if self.counter[val] > 0:
            return False 
        self.counter[val] += len(self.list)+1
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if self.counter[val] == 0:
            return False 
        temp = self.list[-1]
        self.list[self.counter[val]-1] = temp
        self.counter[temp] = self.counter[val]
        self.counter[val] = 0
        self.list.pop()
        #print(self.list, self.counter)
        return True
        
    def getRandom(self) -> int:
        return self.list[random.randint(0, len(self.list)-1)]        
