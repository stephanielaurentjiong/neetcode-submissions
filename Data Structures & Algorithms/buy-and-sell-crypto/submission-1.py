class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if len(prices) == 1:
        #     return 0
        
        l = 0
        r = 1
        maxProfit = 0
        bestBuy = float("inf") 

        while r < len(prices):
            bestBuy = min(prices[l], bestBuy)
            print("bestbuy", bestBuy)

            potential = prices[r] - bestBuy 

            print("potential", potential)

            if potential > maxProfit: 
                maxProfit = potential
            
            l += 1
            r += 1

            print("maxProfit",  maxProfit)
        
        return maxProfit



