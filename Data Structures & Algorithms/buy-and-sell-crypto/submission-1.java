class Solution {
    public int maxProfit(int[] prices) {

        int buyingPrice = prices[0];
        int maxProfit = 0;

        for (int price = 1; price < prices.length; price++) {
            int profit = prices[price] - buyingPrice;

            if (profit < 0) {
                buyingPrice = prices[price];
            }

            maxProfit = Math.max(profit, maxProfit);
        }
        
        return maxProfit;
    }
}