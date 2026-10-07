class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, to_buy, n = 0, 0, len(prices)
        for to_sell in range(1, n):
            max_profit = max(max_profit, prices[to_sell] - prices[to_buy])
            if (prices[to_buy] > prices[to_sell]):
                to_buy = to_sell 
        return max_profit 