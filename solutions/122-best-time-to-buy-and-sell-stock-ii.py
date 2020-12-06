class Solution:
    def maxProfit(self, prices):
        best_without_stock, best_with_stock = 0, float("-inf")
        for price in prices:
            best_without_stock = max(best_without_stock, best_with_stock + price)
            best_with_stock = max(best_with_stock, best_without_stock - price)
        return best_without_stock