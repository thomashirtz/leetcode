class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s = ' ' + s
        p = ' ' + p
        dp = [[False] * len(p) for _ in range(len(s))]
        dp[0][0] = True

        for j in range(1, len(p)):
            if p[j] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, len(s)):
            for j in range(1, len(p)):
                if p[j] in {s[i], '.'}:
                    dp[i][j] = dp[i - 1][j - 1]
                if p[j] == '*':
                    dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and p[j - 1] in {s[i], '.'})

        return dp[-1][-1]


examples = [
    ["aa", "aa"],
    ["aab", "a*b"]
           ]

for example in examples:
    print(Solution().isMatch(*example))
