class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyingPrice = prices[0]
        profit = 0

        for price in prices:
            if price < buyingPrice:
                buyingPrice = price

            profit = max(profit, price - buyingPrice)

        return profit
