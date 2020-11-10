from typing import List
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        num = [str(x) for x in nums]
        key = cmp_to_key(lambda a, b: ((b + a) > (a + b)) - ((b + a) < (a + b)))
        num.sort(key=key)
        return ''.join(num).lstrip('0') or '0'


examples = [[10, 2], [3, 30, 34, 5, 9], [1], [10]]
for example in examples:
    print(Solution().largestNumber(example))
