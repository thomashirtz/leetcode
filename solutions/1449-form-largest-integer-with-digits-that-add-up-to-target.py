class Solution:
    def largestNumber(self, cost, target):
        dp = [-1]*(target+1)
        for j in range(len(cost)):
            if cost[j] <= target:
                dp[cost[j]] = max(dp[cost[j]], (j+1))
        for i in range(len(dp)):
            for j in range(len(cost)):
                if i+cost[j] <= target and dp[i] != -1:
                    dp[i+cost[j]] = max(dp[i+cost[j]], (j+1)+dp[i]*10)
        if dp[target] ==-1:
            return "0"
        return str(dp[target])