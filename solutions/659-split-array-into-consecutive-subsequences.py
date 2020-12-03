from collections import Counter, defaultdict
from typing import List

# Explanation https://www.youtube.com/watch?v=uJ8BAQ8lASE&ab_channel=NideeshTerapalli

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        frequency = dict(Counter(nums))
        hypothetical = defaultdict(int)
        for num in nums:
            if frequency.get(num, 0) > 0:
                if hypothetical.get(num, 0) > 0:
                    frequency[num] -= 1
                    hypothetical[num] -= 1
                    hypothetical[num + 1] += 1
                else:
                    for i in [0, 1, 2]:
                        if frequency.get(num + i, 0) > 0:
                            frequency[num + i] -= 1
                        else:
                            return False
                    hypothetical[num + 3] += 1
        return True


examples = [
    [1, 2, 3, 3, 4, 5],
    [1, 2, 3, 3, 4, 4, 5, 5],
    [1, 2, 3, 4, 4, 5]
]

for example in examples:
    print(Solution().isPossible(example))