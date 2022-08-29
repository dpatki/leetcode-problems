#sumbitted 30/05/2022

class StockSpanner:

    def __init__(self):
        self.day = 0
        self.stack = []

    def next(self, price: int) -> int:
        #print(self.stack, price, self.day)
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        if len(self.stack) == 0:
            self.stack.append((price, self.day))
            self.day += 1
            return self.day
        else:
            res = self.day-self.stack[-1][1]
            self.stack.append((price, self.day))
            self.day += 1
            return res