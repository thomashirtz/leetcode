from collections import Counter

class Solution:
    def findLucky(self, nums):
        counter = Counter(nums)
        answer = -1
        for k, v in dict(counter).items():
            if k == v:
                answer = max(answer, k)
        return answer
