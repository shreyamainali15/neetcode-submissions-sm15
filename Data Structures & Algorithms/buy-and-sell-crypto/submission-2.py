class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buyingPrice = prices[0]

        for price in prices:
            if buyingPrice > price:
                buyingPrice = price

            profit = price - buyingPrice 

            max_profit = max(profit, max_profit)

        return max_profit