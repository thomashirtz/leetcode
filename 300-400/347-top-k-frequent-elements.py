from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        return [x for x, y in counter.most_common(k)]
        
        
nums = [1,1,1,2,2,3]
k = 1
print(Solution().topKFrequent(nums, k))

nums = [1]
k = 1
print(Solution().topKFrequent(nums, k))