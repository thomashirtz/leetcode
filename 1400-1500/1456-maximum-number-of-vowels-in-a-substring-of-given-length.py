class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        dp = [0] + [1 if c in ('a', 'e', 'i', 'o', 'u') else 0 for c in s]
        for i in range(len(dp) - 1):
            dp[i + 1] = dp[i + 1] + dp[i]
        answer = 0
        for i in range(len(dp) - k):
            answer = max(answer, dp[i + k] - dp[i])
        return answer


examples = [["abciiidef", 3], ["leetcode", 3]]

for example in examples:
    print(Solution().maxVowels(*example))