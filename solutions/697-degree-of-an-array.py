from collections import Counter


class Solution:
    def findShortestSubArray(self, nums):

        def rindex(mylist, myvalue):
            return len(mylist) - mylist[::-1].index(myvalue) - 1

        counter = Counter(nums)
        maximum = max(counter.values())
        answer = float('inf')

        for k, v in counter.items():
            if v == maximum:
                answer = min(answer, rindex(nums, k) - nums.index(k))

        return answer + 1
