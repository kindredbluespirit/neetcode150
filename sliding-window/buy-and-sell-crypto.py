class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        p_min = math.inf
        # p_max = -math.inf

        for p in prices:

            if p < p_min:
                p_min = p
            
            profit = p - p_min

            if profit > max_profit:
                max_profit = profit
        
        return max_profit
        
