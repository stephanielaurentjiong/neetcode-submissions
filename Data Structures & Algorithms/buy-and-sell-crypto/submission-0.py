class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0;
        while (r < len(prices)):
            if prices[l] < prices[r]:
                prof = prices[r] - prices[l];
                maxP = max(maxP, prof)
            else:
                l = r #This line is for setting the smallest price to buy
            r += 1;
        
        return maxP
