class Solution {
    public int maxProfit(int[] prices) {
        int buy = prices[0];
        int maxprofit = 0;
        for (int i = 0; i < prices.length; i++) {
            buy = Math.min(prices[i], buy);
            maxprofit = Math.max(prices[i] - buy, maxprofit);
        }
        return maxprofit;
    }
}