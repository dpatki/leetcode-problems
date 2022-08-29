#submitted 07/06/2022

class RandomizedCollection:

    def __init__(self):
        self.indexes = defaultdict(set)
        self.list = []
        self.counter = Counter()

    def insert(self, val: int) -> bool:
        inset = True
        if self.counter[val] != 0:
            inset = False 
        self.indexes[val].add(len(self.list))
        self.list.append(val)
        self.counter[val] += 1
        return inset
        
    def remove(self, val: int) -> bool:
        if self.counter[val] == 0:
            return False 
        index = self.indexes[val].pop()
        value = self.list[-1]
        self.list[index] = value
        self.indexes[value].discard(len(self.list)-1)
        self.indexes[value].add(index)
        self.list.pop()
        self.counter[val] -= 1
        return True

    def getRandom(self) -> int:
        return self.list[random.randint(0, len(self.list)-1)]