class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice = prices[0]
        max_profit = 0

        for price in prices:
            if price < buyPrice:
                buyPrice = price

            max_profit = max(max_profit, price - buyPrice)

        return max_profit