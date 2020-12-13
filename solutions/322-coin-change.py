class Solution:
    def coinChange(self, coins, amount):
        dp = [0]+[amount+1]*amount
        for i in range(len(dp)):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        return [dp[amount], -1][dp[amount] == amount+1]