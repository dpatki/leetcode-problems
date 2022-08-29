#submitted 24/08/2022

class Solution:

    def __init__(self, w: List[int]):
        self.list = [i for i in range(len(w))]
        self.weight = w

    def pickIndex(self) -> int:
        return random.choices(self.list, self.weight)[0]
