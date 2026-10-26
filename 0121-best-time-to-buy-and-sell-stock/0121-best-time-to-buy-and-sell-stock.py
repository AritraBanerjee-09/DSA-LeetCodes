class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        min_profit = prices[0]
        max_profit = 0

        for p in prices:
            if p < min_profit:
                min_profit = p
        
            profit = p - min_profit

            if profit > max_profit:
                max_profit = profit
    
        return max_profit