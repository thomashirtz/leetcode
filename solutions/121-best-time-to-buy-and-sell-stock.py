class Solution:
    def maxProfit(self, prices):
        profit, min_value = 0, float("inf")
        for price in prices:
            if price < min_value:
                min_value = price
            elif price - min_value > profit:
                profit = price - min_value
        return profit
