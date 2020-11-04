from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for _ in range(k):
            nums.insert(0, nums[-1])
            del nums[-1]
        return nums


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]


examples = [
    [[1, 2, 3, 4, 5, 6, 7], 3]
]

for example in examples:
    print(Solution().rotate(*example))