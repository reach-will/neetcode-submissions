class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        curr_min = prices[0]
        for p in prices:
            if p < curr_min:
                curr_min = p
            if p - curr_min > max_profit:
                max_profit = p - curr_min
        return max_profit