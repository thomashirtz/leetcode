class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high + 1) // 2 - low // 2


examples = [[3,7], [8,10]]
for example in examples:
    print(Solution().countOdds(*example))
