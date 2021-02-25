#submitted 02/07/2021
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        i = 0
        listy = []
        while i < len(prices):
    #print(prices[i], prices[fixed])
    
            while listy and prices[listy[len(listy)-1]] >= prices[i]:
                prices[listy[(len(listy)-1)]] -= prices[i]
                listy.pop()
     
   
            listy.append(i)
            i += 1
  
        return prices
