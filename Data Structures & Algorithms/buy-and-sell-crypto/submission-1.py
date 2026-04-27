class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices = sorted(prices)
        buy_price = min(prices)
        sell_price = max(prices[prices.index(buy_price):])
        max_profit = sell_price - buy_price
        return max_profit