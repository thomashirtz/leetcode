import math

class Solution:
    def numSquares(self, n):
        dp = [0]+[float('inf')]*n
        for x in range(n+1):
            sqrt = math.sqrt(x)
            if sqrt.is_integer():
                dp[x] = 1
            else:
                dp[x] = min(dp[x-i*i] + 1 for i in range(1, math.ceil(sqrt)))
        return dp[n]

print(Solution().numSquares(12))

print(Solution().numSquares(13))