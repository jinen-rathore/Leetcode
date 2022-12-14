class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = float('inf')
        profit = 0
        for i in prices:
            profit = max(profit, i-low)
            low = min(low, i)
        return profit